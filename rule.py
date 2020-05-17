def black_point(overlap_check_arr,x,y): # 흑돌 입장에서 백돌 방어
    sum = 0
    for i in range(0,2):
        if i == 0:
            n1 = -1
            n2 = -50
            n3 = -5000
            n4 = -50000
            n5 = -500000
            color = 1
            enemy_color = 2
        elif i == 1:
            n1 = -1
            n2 = -50
            n3 = -5500
            n4 = -900000
            n5 = -999999
            color = 2
            enemy_color = 1
        # 세로 상 체크
        if overlap_check_arr[x-1][y] == color:
            sum += n1
            if overlap_check_arr[x-2][y] == color:
                sum += n2
                if overlap_check_arr[x-3][y] == color:
                    sum += n3
                    if overlap_check_arr[x-4][y] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x-4][y] == color:
                        sum += n4
                        if overlap_check_arr[x-5][y] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x-5][y] == color:
                            sum += n5
        # 세로 하 체크
        if overlap_check_arr[x+1][y] == color:
            sum += n1
            if overlap_check_arr[x+2][y] == color:
                sum += n2
                if overlap_check_arr[x+3][y] == color:
                    sum += n3
                    if overlap_check_arr[x+4][y] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x+4][y] == color:
                        sum += n4
                        if overlap_check_arr[x+5][y] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x+5][y] == color:
                            sum += n5
        # 가로 좌 체크
        if overlap_check_arr[x][y-1] == color:
            sum += n1
            if overlap_check_arr[x][y-2] == color:
                sum += n2
                if overlap_check_arr[x][y-3] == color:
                    sum += n3
                    if overlap_check_arr[x][y-4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x][y-4] == color:
                        sum += n4
                        if overlap_check_arr[x][y-5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x][y-5] == color:
                            sum += n5
        # 가로 우 체크
        if overlap_check_arr[x][y+1] == color:
            sum += n1
            if overlap_check_arr[x][y+2] == color:
                sum += n2
                if overlap_check_arr[x][y+3] == color:
                    sum += n3
                    if overlap_check_arr[x][y+4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x][y+4] == color:
                        sum += n4
                        if overlap_check_arr[x][y+5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x][y+5] == color:
                            sum += n5
        # 대각선 좌상 체크
        if overlap_check_arr[x-1][y-1] == color:
            sum += n1
            if overlap_check_arr[x-2][y-2] == color:
                sum += n2
                if overlap_check_arr[x-3][y-3] == color:
                    sum += n3
                    if overlap_check_arr[x-4][y-4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x-4][y-4] == color:
                        sum += n4
                        if overlap_check_arr[x-5][y-5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x-5][y-5] == color:
                            sum += n5
        # 대각선 좌하 체크
        if overlap_check_arr[x+1][y-1] == color:
            sum += n1
            if overlap_check_arr[x+2][y-2] == color:
                sum += n2
                if overlap_check_arr[x+3][y-3] == color:
                    sum += n3
                    if overlap_check_arr[x+4][y-4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x+4][y-4] == color:
                        sum += n4
                        if overlap_check_arr[x+5][y-5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x+5][y-5] == color:
                            sum += n5
        # 대각선 우상 체크
        if overlap_check_arr[x-1][y+1] == color:
            sum += n1
            if overlap_check_arr[x-2][y+2] == color:
                sum += n2
                if overlap_check_arr[x-3][y+3] == color:
                    sum += n3
                    if overlap_check_arr[x-4][y+4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x-4][y+4] == color:
                        sum += n4
                        if overlap_check_arr[x-5][y+5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x-5][y+5] == color:
                            sum += n5
        # 대각선 우하 체크
        if overlap_check_arr[x+1][y+1] == color:
            sum += n1
            if overlap_check_arr[x+2][y+2] == color:
                sum += n2
                if overlap_check_arr[x+3][y+3] == color:
                    sum += n3
                    if overlap_check_arr[x+4][y+4] == enemy_color:
                        sum += 500
                    if overlap_check_arr[x+4][y+4] == color:
                        sum += n4
                        if overlap_check_arr[x+5][y+5] == enemy_color:
                            sum += 5000
                        if overlap_check_arr[x+5][y+5] == color:
                            sum += n5

    if prohibited_play(overlap_check_arr,x,y,2):
        sum = 0
    return sum

def white_point(overlap_check_arr,x,y): # 백돌 입장에서 흑돌 방어
    sum = 0
    for i in range(0,2):
        # 가로 좌 체크
        if i == 0:
            n1 = 1
            n2 = 50
            n3 = 5000
            n4 = 50000
            n5 = 500000
            color = 2
            enemy_color = 1
        elif i == 1:
            n1 = 1
            n2 = 50
            n3 = 5500
            n4 = 900000
            n5 = 999999
            color = 1
            enemy_color = 2
        # 세로 상 체크
        if overlap_check_arr[x - 1][y] == color:
            sum += n1
            if overlap_check_arr[x - 2][y] == color:
                sum += n2
                if overlap_check_arr[x - 3][y] == color:
                    sum += n3
                    if overlap_check_arr[x - 4][y] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x - 4][y] == color:
                        sum += n4
                        if overlap_check_arr[x - 5][y] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x - 5][y] == color:
                            sum += n5
        # 세로 하 체크
        if overlap_check_arr[x + 1][y] == color:
            sum += n1
            if overlap_check_arr[x + 2][y] == color:
                sum += n2
                if overlap_check_arr[x + 3][y] == color:
                    sum += n3
                    if overlap_check_arr[x + 4][y] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x + 4][y] == color:
                        sum += n4
                        if overlap_check_arr[x + 5][y] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x + 5][y] == color:
                            sum += n5
        # 가로 좌 체크
        if overlap_check_arr[x][y - 1] == color:
            sum += n1
            if overlap_check_arr[x][y - 2] == color:
                sum += n2
                if overlap_check_arr[x][y - 3] == color:
                    sum += n3
                    if overlap_check_arr[x][y - 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x][y - 4] == color:
                        sum += n4
                        if overlap_check_arr[x][y - 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x][y - 5] == color:
                            sum += n5
        # 가로 우 체크
        if overlap_check_arr[x][y + 1] == color:
            sum += n1
            if overlap_check_arr[x][y + 2] == color:
                sum += n2
                if overlap_check_arr[x][y + 3] == color:
                    sum += n3
                    if overlap_check_arr[x][y + 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x][y + 4] == color:
                        sum += n4
                        if overlap_check_arr[x][y + 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x][y + 5] == color:
                            sum += n5
        # 대각선 좌상 체크
        if overlap_check_arr[x - 1][y - 1] == color:
            sum += n1
            if overlap_check_arr[x - 2][y - 2] == color:
                sum += n2
                if overlap_check_arr[x - 3][y - 3] == color:
                    sum += n3
                    if overlap_check_arr[x - 4][y - 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x - 4][y - 4] == color:
                        sum += n4
                        if overlap_check_arr[x - 5][y - 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x - 5][y - 5] == color:
                            sum += n5
        # 대각선 좌하 체크
        if overlap_check_arr[x + 1][y - 1] == color:
            sum += n1
            if overlap_check_arr[x + 2][y - 2] == color:
                sum += n2
                if overlap_check_arr[x + 3][y - 3] == color:
                    sum += n3
                    if overlap_check_arr[x + 4][y - 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x + 4][y - 4] == color:
                        sum += n4
                        if overlap_check_arr[x + 5][y - 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x + 5][y - 5] == color:
                            sum += n5
        # 대각선 우상 체크
        if overlap_check_arr[x - 1][y + 1] == color:
            sum += n1
            if overlap_check_arr[x - 2][y + 2] == color:
                sum += n2
                if overlap_check_arr[x - 3][y + 3] == color:
                    sum += n3
                    if overlap_check_arr[x - 4][y + 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x - 4][y + 4] == color:
                        sum += n4
                        if overlap_check_arr[x - 5][y + 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x - 5][y + 5] == color:
                            sum += n5
        # 대각선 우하 체크
        if overlap_check_arr[x + 1][y + 1] == color:
            sum += n1
            if overlap_check_arr[x + 2][y + 2] == color:
                sum += n2
                if overlap_check_arr[x + 3][y + 3] == color:
                    sum += n3
                    if overlap_check_arr[x + 4][y + 4] == enemy_color:
                        sum -= 500
                    if overlap_check_arr[x + 4][y + 4] == color:
                        sum += n4
                        if overlap_check_arr[x + 5][y + 5] == enemy_color:
                            sum -= 5000
                        if overlap_check_arr[x + 5][y + 5] == color:
                            sum += n5

    if prohibited_play(overlap_check_arr,x,y,1):
        sum = 0
    return sum

def victory_check(overlap_check_arr): # 승리조건 체크 함수
    sum = 0
    for i in range(1,3):
        color = i
        for x in range(0,19):
            for y in range(0,19):
                    # 세로 상 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x-1][y] == color:
                        sum += 1
                        if overlap_check_arr[x - 2][y] == color:
                            sum += 1
                            if overlap_check_arr[x - 3][y] == color:
                                sum += 1
                                if overlap_check_arr[x - 4][y] == color:
                                    sum += 1
                                    if overlap_check_arr[x + 1][y] == color:
                                        sum += 1
                                    if overlap_check_arr[x - 5][y] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 세로 하 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x + 1][y] == color:
                        sum += 1
                        if overlap_check_arr[x + 2][y] == color:
                            sum += 1
                            if overlap_check_arr[x + 3][y] == color:
                                sum += 1
                                if overlap_check_arr[x + 4][y] == color:
                                    sum += 1
                                    if overlap_check_arr[x - 1][y] == color:
                                        sum += 1
                                    if overlap_check_arr[x + 5][y] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 가로 좌 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x][y - 1] == color:
                        sum += 1
                        if overlap_check_arr[x][y - 2] == color:
                            sum += 1
                            if overlap_check_arr[x][y - 3] == color:
                                sum += 1
                                if overlap_check_arr[x][y - 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x][y + 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x][y - 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 가로 우 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x][y + 1] == color:
                        sum += 1
                        if overlap_check_arr[x][y + 2] == color:
                            sum += 1
                            if overlap_check_arr[x][y + 3] == color:
                                sum += 1
                                if overlap_check_arr[x][y + 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x][y - 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x][y + 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 대각선 좌상 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x - 1][y - 1] == color:
                        sum += 1
                        if overlap_check_arr[x - 2][y - 2] == color:
                            sum += 1
                            if overlap_check_arr[x - 3][y - 3] == color:
                                sum += 1
                                if overlap_check_arr[x - 4][y - 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x + 1][y + 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x - 5][y - 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 대각선 좌하 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x + 1][y - 1] == color:
                        sum += 1
                        if overlap_check_arr[x + 2][y - 2] == color:
                            sum += 1
                            if overlap_check_arr[x + 3][y - 3] == color:
                                sum += 1
                                if overlap_check_arr[x + 4][y - 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x -1][y + 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x + 5][y - 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 대각선 우상 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x - 1][y + 1] == color:
                        sum += 1
                        if overlap_check_arr[x - 2][y + 2] == color:
                            sum += 1
                            if overlap_check_arr[x - 3][y + 3] == color:
                                sum += 1
                                if overlap_check_arr[x - 4][y + 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x + 1][y - 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x - 5][y + 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
                    # 대각선 우하 체크
                if overlap_check_arr[x][y] == color:
                    sum += 1
                    if overlap_check_arr[x + 1][y + 1] == color:
                        sum += 1
                        if overlap_check_arr[x + 2][y + 2] == color:
                            sum += 1
                            if overlap_check_arr[x + 3][y + 3] == color:
                                sum += 1
                                if overlap_check_arr[x + 4][y + 4] == color:
                                    sum += 1
                                    if overlap_check_arr[x - 1][y - 1] == color:
                                        sum += 1
                                    if overlap_check_arr[x + 5][y + 5] == color:
                                        sum +=1
                if sum == 5:
                    return True
                else:
                    sum = 0
    return False

def prohibited_play(a,x,y,color): # 쌍삼 금지수 체크
    if color == 1:
        enemy_color = 2
    elif color == 2:
        enemy_color = 1
    if a[x][y-1] == color and a[x][y-2] == color and a[x-1][y] == color and a[x-2][y] == color and a[x][y-3] != enemy_color and a[x-3][y] != enemy_color: # 90도 쌍삼
        return True
    elif a[x-1][y] == color and a[x-2][y] == color and a[x][y+1] == color and a[x][y+2] == color and a[x-3][y] != enemy_color and a[x][y+3] != enemy_color:
        return True
    elif a[x][y-1] == color and a[x][y-2] == color and a[x+1][y] == color and a[x+2][y] == color and a[x][y-3] != enemy_color and a[x+3][y] != enemy_color:
        return True
    elif a[x][y+1] == color and a[x][y+2] == color and a[x+1][y] == color and a[x+2][y] == color and a[x][y+3] != enemy_color and a[x+3][y] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x+1][y-1] == color and a[x+2][y-2] == color and a[x-3][y-3] != enemy_color and a[x+3][y-3] != enemy_color:
        return True
    elif a[x+1][y-1] == color and a[x+2][y-2] == color and a[x+1][y+1] == color and a[x+2][y+2] == color and a[x+3][y-3] != enemy_color and a[x+3][y+3] != enemy_color:
        return True
    elif a[x+1][y+1] == color and a[x+2][y+2] == color and a[x-1][y+1] == color and a[x-2][y+2] == color and a[x+3][y+3] != enemy_color and a[x-3][y+3] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x-1][y+1] == color and a[x-2][y+2] == color and a[x-3][y-3] != enemy_color and a[x-3][y+3] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x-1][y] == color and a[x-2][y] == color and a[x-3][y-3] != enemy_color and a[x-3][y] != enemy_color: # 45도 쌍삼
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x][y-1] == color and a[x][y-2] == color and a[x-3][y-3] != enemy_color and a[x][y-3] != enemy_color:
        return True
    elif a[x][y-1] == color and a[x][y-2] == color and a[x+1][y-1] == color and a[x+2][y-2] == color and a[x][y-3] != enemy_color and a[x+3][y-3] != enemy_color:
        return True
    elif a[x+1][y-1] == color and a[x+2][y-2] == color and a[x+1][y] == color and a[x+2][y] == color and a[x+3][y-3] != enemy_color and a[x+3][y] != enemy_color:
        return True
    elif a[x+1][y] == color and a[x+2][y] == color and a[x+1][y+1] == color and a[x+2][y+2] == color and a[x+3][y] != enemy_color and a[x+3][y+3] != enemy_color:
        return True
    elif a[x+1][y+1] == color and a[x+2][y+2] == color and a[x][y+1] == color and a[x][y+2] == color and a[x+3][y+3] != enemy_color and a[x][y+3] != enemy_color:
        return True
    elif a[x][y+1] == color and a[x][y+2] == color and a[x-1][y+1] == color and a[x-2][y+2] == color and a[x][y+3] != enemy_color and a[x-3][y+3] != enemy_color:
        return True
    elif a[x-1][y+1] == color and a[x-2][y+2] == color and a[x-1][y] == color and a[x-2][y] == color and a[x-3][y+3] != enemy_color and a[x-3][y] != enemy_color:
        return True
    elif a[x][y-1] == color and a[x][y-2] == color and a[x-1][y+1] == color and a[x-2][y+2] == color and a[x][y-3] != enemy_color and a[x-3][y+3] != enemy_color: # 135도 쌍삼
        return True
    elif a[x-1][y] == color and a[x-2][y] == color and a[x+1][y-1] == color and a[x+2][y-2] == color and a[x-3][y] != enemy_color and a[x+3][y-3] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x+1][y] == color and a[x+2][y] == color and a[x-3][y-3] != enemy_color and a[x+3][y] != enemy_color:
        return True
    elif a[x][y-1] == color and a[x][y-2] == color and a[x+1][y+1] == color and a[x+2][y+2] == color and a[x][y-3] != enemy_color and a[x+3][y+3] != enemy_color:
        return True
    elif a[x+1][y-1] == color and a[x+2][y-2] == color and a[x][y+1] == color and a[x][y+2] == color and a[x+3][y-3] != enemy_color and a[x][y+3] != enemy_color:
        return True
    elif a[x+1][y] == color and a[x+2][y] == color and a[x-1][y+1] == color and a[x-2][y+2] == color and a[x+3][y] != enemy_color and a[x-3][y+3] != enemy_color:
        return True
    elif a[x-1][y] == color and a[x-2][y] == color and a[x+1][y+1] == color and a[x+2][y+2] == color and a[x-3][y] != enemy_color and a[x+3][y+3] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-2][y-2] == color and a[x][y+1] == color and a[x][y+2] == color and a[x-3][y-3] != enemy_color and a[x][y+3] != enemy_color:
        return True
    elif a[x-1][y-1] == color and a[x-1][y+1] == color and a[x+1][y-1] == color and a[x+1][y+1] == color and a[x-2][y-2] != enemy_color and a[x-2][y+2] != enemy_color and a[x+2][y-2] != enemy_color and a[x+2][y+2] != enemy_color: #십자가 모양 쌍삼
        return True
    elif a[x-1][y] == color and a[x][y-1] == color and a[x+1][y] == color and a[x][y+1] == color and a[x-2][y] != enemy_color and a[x][y-2] != enemy_color and a[x+2][y] != enemy_color and a[x][y+2] != color:
        return True
    else:
        return False