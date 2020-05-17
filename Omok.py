from tkinter import * # GUI 구현
import tkinter.messagebox # 메세지 박스
import copy # deepcopy 사용
import numpy as np # np.array 사용
import time # time.time() 사용
import rule # 오목 게임룰과 evaluation function
import math # math.floor() 사용 - 버림 함수
import threading # threading.Timer 사용 - 일정 시간마다 실행되는 함수


first_player_turn = True # 플레이어와 AI의 턴을 구분
first_player_turn_AI = False # True인 경우 AI가 흑돌, False인 경우 AI가 백돌
overlap_check_arr = [[0 for i in range(24)] for j in range(24)] # list index out of range 문제를 해결하기 위해 24X24사이즈 배열 생성
overlap_check_arr_depth3 = [[0 for i in range(24)] for j in range(24)] # deepcopy에 쓰이는 array
overlap_check_arr_depth2 = [[0 for i in range(24)] for j in range(24)] # deepcopy에 쓰이는 array
overlap_check_arr_depth1 = [[0 for i in range(24)] for j in range(24)] # deepcopy에 쓰이는 array
evaluation_arr = ([[0 for i in range(19)] for j in range(19)]) # evaluation 값이 저장되는 array
evaluation_list = [] # child node가 저장될 array

AI_turn = False # 상대를 AI로 할지 결정

start_time = time.time() # 게임 시작시간
game_ending = False # 게임이 끝나면 True

infinity = 99999999
# color 1 = 흑돌, 2 = 백돌

def show_overlap_arr(): # 바둑판 현황
    for i in range(0,19):
        for j in range(0,19):
            print(overlap_check_arr[i][j], end='')
            if (j==18):
                print()

def show_evaluation_arr(): # 평가판 현황
    for i in range(0,19):
        for j in range(0,19):
            print("%5s"%(evaluation_arr[i][j]), end='')
            if (j==18):
                print()
    print("\n\n\n")


######################################################### Alpha Beta pruning Alg

def max_value(a,b):
    max = a
    if (max < b):
        max = b
    return max

def min_value(a,b):
    min = a
    if (min > b):
        min = b
    return min

def alpha_beta(copy_overlap_check_arr, evaluation_list, depth, a, b, maximizingPlayer): # Alpha_Beta pruning search Alg
    global overlap_check_arr_depth3
    global overlap_check_arr_depth2
    global overlap_check_arr_depth1
    global first_player_turn
    limited_time = math.floor(11 - (time.time() - start_time)) # AI턴 시간제한 체크
    if depth == 0: # depth가 0인 경우
        return np.max(evaluation_list[:,2])
    if rule.victory_check(overlap_check_arr): # 게임에 승리한 경우
        return np.max(evaluation_list[:,2])
    if maximizingPlayer:
        v = -infinity
        for child in evaluation_list:
            if depth == 3:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth3 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth3[child[0]][child[1]] = 2
                first_player_turn = TRUE
                evaluate_all(overlap_check_arr_depth3)
                v = max_value(v, alpha_beta(overlap_check_arr_depth3, evaluation_list, depth - 1, a, b, FALSE))
                a = max_value(a, v)
                if b <= a:
                    break
            elif depth == 2:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth2 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth2[child[0]][child[1]] = 2
                first_player_turn = TRUE
                evaluate_all(overlap_check_arr_depth2)
                v = max_value(v, alpha_beta(overlap_check_arr_depth2, evaluation_list, depth - 1, a, b, FALSE))
                a = max_value(a, v)
                if b <= a:
                    break
            elif depth == 1:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth1 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth1[child[0]][child[1]] = 2
                first_player_turn = TRUE
                evaluate_all(overlap_check_arr_depth1)
                v = max_value(v, alpha_beta(overlap_check_arr_depth1, evaluation_list, depth - 1, a, b, FALSE))
                a = max_value(a, v)
                if b <= a:
                    break
        return v
    else:
        v = infinity
        for child in evaluation_list:
            if depth == 3:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth3 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth3[child[0]][child[1]] = 1
                first_player_turn = FALSE
                evaluate_all(overlap_check_arr_depth3)
                v = min_value(v, alpha_beta(overlap_check_arr_depth3, evaluation_list, depth - 1, a, b, TRUE))
                a = min_value(a, v)
                if b <= a:
                    break
            elif depth == 2:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth2 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth2[child[0]][child[1]] = 1
                first_player_turn = FALSE
                evaluate_all(overlap_check_arr_depth2)
                v = min_value(v, alpha_beta(overlap_check_arr_depth2, evaluation_list, depth - 1, a, b, TRUE))
                a = min_value(a, v)
                if b <= a:
                    break
            elif depth == 1:
                if limited_time < 2:
                    return 0
                overlap_check_arr_depth1 = copy.deepcopy(copy_overlap_check_arr)
                overlap_check_arr_depth1[child[0]][child[1]] = 1
                first_player_turn = FALSE
                evaluate_all(overlap_check_arr_depth1)
                v = min_value(v, alpha_beta(overlap_check_arr_depth1, evaluation_list, depth - 1, a, b, TRUE))
                a = min_value(a, v)
                if b <= a:
                    break
        return v

def iterative_deepening(copy_overlap_check_arr, evaluation_list, a, b, maximizingPlayer): # Iterative Deepening Search Alg
    max = 0
    for depth in range(0,4): # depth => 0, 1, 2, 3 ...
        result = alpha_beta(copy_overlap_check_arr, evaluation_list, depth, a, b, maximizingPlayer)
        if result != 0:
            max = result
    return max


def AI(): # AI턴에 실행 Iterative Deepening과 Alpha_Beta 호출
    global overlap_check_arr
    global evaluation_list
    global first_player_turn
    global start_time
    global AI_turn
    copy_overlap_check_arr = copy.deepcopy(overlap_check_arr)
    a = -infinity
    b = infinity
    maximizingPlayer = True
    v = iterative_deepening(copy_overlap_check_arr, evaluation_list, a, b, maximizingPlayer)
    if first_player_turn_AI == False:
        first_player_turn = False
    else:
        first_player_turn = True
    evaluate_all(overlap_check_arr)
    for child in evaluation_list:
        if (child[2] == v):
            x = child[0]
            y = child[1]
            position_x = x*30 + 30
            position_y = y*30 + 30
            overlap_check(x,y)
            put_checker(position_x, position_y)
            evaluate_all(overlap_check_arr)
            break
    if rule.victory_check(overlap_check_arr): # 게임 승리시 실행
        victory_msg()
    start_time = time.time() # start_time 초기화
    AI_turn = False # AI turn 종료


########################################################## Evaluation Function

def _evaluation(i,j): # evaluation value 계산, rule.py의 black_point와 white_point 호출
    evaluation = 0
    global overlap_check_arr

    if first_player_turn_AI == False and first_player_turn == False: # 플레이어 = 흑돌 , AI 차례
        evaluation += rule.white_point(overlap_check_arr,i, j)
    elif first_player_turn_AI == False and first_player_turn == True: # 플레이어 = 흑돌, 플레이어 차례
        evaluation += rule.black_point(overlap_check_arr,i, j)
    if first_player_turn_AI == True and first_player_turn == False: # 플레이어 = 백돌, 플레이어 차례
        evaluation += rule.black_point(overlap_check_arr,i, j)
    elif first_player_turn_AI == True and first_player_turn == True: # 플레이어 = 백돌, AI 차례
        evaluation += rule.white_point(overlap_check_arr, i, j)
    return evaluation

def evaluation(arr,x, y): # 돌이 놓인 곳의 주변을 탐색, evaluation 내장함수 호출
    global evaluation_arr
    global evaluation_list
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if arr[i][j] == 0:
                if i < 0 or j < 0:
                    pass
                elif i > 18 or j > 18:
                    pass
                else:
                    evaluation_arr[i][j] = _evaluation(i,j)
                    evaluation_list.append([j, i, evaluation_arr[i][j]])



def evaluate_all(arr): # 평가판 함수 작성(evaluation_arr), evaluation 함수 호출
    global evaluation_list
    global evaluation_arr
    evaluation_list = []
    evaluation_arr = [[0 for i in range(19)] for j in range(19)]
    for i in range(0,19):
        for j in range(0,19):
            if arr[i][j] != 0:
                if arr[i][j] == 1:
                    evaluation_arr[i][j] = 'B'
                elif arr[i][j] == 2:
                    evaluation_arr[i][j] = "W"
                evaluation(arr,i,j)
    evaluation_list = np.array(evaluation_list)
    show_evaluation_arr()
########################################################## OMOK GUI


def victory_msg(): # 승리조건 달성시 메세지 출력
    global game_ending
    if (first_player_turn == True):
        win_checker = "백"
    else:
        win_checker  = "흑"
    game_ending = True
    tkinter.messagebox.showinfo("게임결과","{}돌 승리!" .format(win_checker))
    window.destroy()


def positionCheck(a): # 마우스 커서의 위치값을 가까운 바둑판 교점의 좌표값으로 변경
    if (30<= a <45):
        return 30
    for i in range(45, 570, 30):
        if (i<= a <i+30):
            return i+15;
    return


def overlap_check(x,y): # 바둑판에 이미 돌이 놓여있는지 확인
    global overlap_check_arr
    if (overlap_check_arr[y][x] == 0):
        if (first_player_turn == True):
            overlap_check_arr[y][x] = 1 # 흑돌이 놓은 곳
        else:
            overlap_check_arr[y][x] = 2 # 백돌이 놓은 곳
        return True
    else:
        return False

def onClick(event): # 마우스 클릭 이벤트 발생시 실행
    global overlap_check_arr
    if AI_turn == False:
        try:
            position_x = positionCheck(event.x)
            position_y = positionCheck(event.y)
            x = ((position_x - 30) // 30)
            y = ((position_y - 30) // 30)
            if first_player_turn == True:
                if rule.prohibited_play(overlap_check_arr,y,x,1): # 쌍삼 체크
                    tkinter.messagebox.showinfo("다른 수를 두세요","쌍삼 입니다!")
                else:
                    play_turn(x,y)

            else:
                if rule.prohibited_play(overlap_check_arr,y,x,2): # 쌍삼 체크
                    tkinter.messagebox.showinfo("다른 수를 두세요","쌍삼 입니다!")
                else:
                    play_turn(x, y)
        except: # 바둑판의 위치를 벗어나는 곳에 마우스 클릭시 경고 메세지
            tkinter.messagebox.showwarning("경고","바둑판 위를 눌러주세요!")


def play_turn(x, y): # 플레이어가 바둑돌을 놓고 쌍삼의 위치가 아닐 경우 실행
    global start_time
    position_x = x*30 + 30
    position_y = y*30 + 30
    if (overlap_check(x,y)):
        put_checker(position_x, position_y)
        canvas.delete('label')
        canvas.create_text(700, 100, text="("+str(y)+","+str(x)+")", font = 20, tags=('label'))
        evaluate_all(overlap_check_arr) # 실제 입력 좌표와 대칭되게 넘겨줘야 함!!!
        if rule.victory_check(overlap_check_arr):
            victory_msg()
        start_time = time.time() #start_time 초기화

def put_checker(x, y): # 쌍삼, 중복수가 아닐 때 canvas위에 바둑돌을 그림
    global first_player_turn
    if (first_player_turn != TRUE):
        first_player_turn = TRUE
        checker_color = "White"
    else:
        first_player_turn = FALSE
        checker_color = "Black"
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill = checker_color)


def clock(): # 시간제한을 알려주는 함수
    global canvas
    canvas.delete('clock')
    limited_time = math.floor(11 - (time.time() - start_time))
    canvas.create_text(700,150,text=limited_time, font=20, tags=('clock'))
    if limited_time < 0:
        if first_player_turn_AI == False and first_player_turn == False and game_ending == False:  # 플레이어 = 흑돌 , AI 차례
            tkinter.messagebox.showinfo("게임결과","시간제한으로 인한 흑돌 승리!")
            window.destroy()
        elif first_player_turn_AI == False and first_player_turn == True and game_ending == False:  # 플레이어 = 흑돌, 플레이어 차례
            tkinter.messagebox.showinfo("게임결과","시간제한으로 인한 백돌 승리!")
            window.destroy()
        if first_player_turn_AI == True and first_player_turn == False and game_ending == False:  # 플레이어 = 백돌, 플레이어 차례
            tkinter.messagebox.showinfo("게임결과","시간제한으로 인한 흑돌 승리!")
            window.destroy()
        elif first_player_turn == True and first_player_turn == True and game_ending == False:  # 플레이어 = 백돌, AI 차례
            tkinter.messagebox.showinfo("게임결과","시간제한으로 인한 백돌 승리!")
            window.destroy()
    t = threading.Timer(1,clock) # 1초마다 호출
    t.setDaemon(True) # main thread is not in main loop 런타임 에러 없애기 위함
    t.start()

def play_AI(): # AI 차례 플레이
    global AI_turn
    if game_ending == False:
        if first_player_turn_AI == False and first_player_turn == False: # 플레이어 = 흑돌, AI 차례
            AI_turn = True
            AI()
        elif first_player_turn_AI == True and first_player_turn == True: # 플레이어 = 백돌, AI 차례
            AI_turn = True
            AI()
    t = threading.Timer(1,play_AI)  # 1초마다 호출
    t.setDaemon(True) # main thread is not in main loop 런타임 에러 없애기 위함
    t.start()



################################################################ main문
window = Tk()
window.title("Omok")
window.resizable(False,False)

canvas = Canvas(window, width = 800, height = 600, bg = "#ffbf80") # 바둑판 생성
canvas.pack(fill="both", expand=True)
for x in range(30, 600, 30):
    canvas.create_line(x, 30, x, 570, fill = "black")
for y in range(30, 600, 30):
    canvas.create_line(30, y, 570, y, fill = "black")
canvas.create_text(650,100, text="좌표")
canvas.create_text(650,150, text="시간제한")
tkinter.messagebox.showinfo("안내사항","1. 10초 이내에 수를 두어야 합니다. (넘어갈 시 패배 처리)\n2. AI 플레이 시 컴퓨터가 수를 둘 때까지 바둑판을 클릭하면 안 됩니다!")
if tkinter.messagebox.askyesno("AI 유무", "상대를 AI로 하시겠습니까?\n(예: AI 상대, 아니오: 플레이어 상대"):
    if tkinter.messagebox.askyesno("선공 정하기", "선공으로 하시겠습니까?"):
        first_player_turn_AI = False
        start_time = math.floor(time.time())
        clock()
    else:
        first_player_turn_AI = True
        start_time = math.floor(time.time())
        clock()
    if first_player_turn_AI:
        put_checker(300,300)
        overlap_check_arr[9][9] = 1
        first_player_turn = False
        evaluate_all(overlap_check_arr)
    play_AI()  # AI 차례 플레이
else:
    start_time = math.floor(time.time())
    clock()
canvas.bind("<Button-1>", onClick);
window.mainloop()