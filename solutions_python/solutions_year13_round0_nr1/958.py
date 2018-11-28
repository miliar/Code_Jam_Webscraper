def check_2(a, b, c, d):
    A = [a, b, c, d]
    
    for i in range(4):
        if (A[i] == 'T'):
            A[i] = 'O'
    return A[0] == 'O' and A[1] == 'O' and A[2] == 'O' and A[3] == 'O'

def check_1(a, b, c, d):
    A = [a, b, c, d]
    
    for i in range(4):
        if (A[i] == 'T'):
            A[i] = 'X'
    return A[0] == 'X' and A[1] == 'X' and A[2] == 'X' and A[3] == 'X'

def solve_X(A):
    res = 0
    
    for i in range(4):
        res = max(res, check_1(A[i][0], A[i][1], A[i][2], A[i][3]), check_1(A[0][i], A[1][i], A[2][i], A[3][i]))
    res = max(res, check_1(A[0][0], A[1][1], A[2][2], A[3][3]))
    res = max(res, check_1(A[3][0], A[2][1], A[1][2], A[0][3]))
    return res

def solve_O(A):
    res = 0
    
    for i in range(4):
        res = max(res, check_2(A[i][0], A[i][1], A[i][2], A[i][3]) or check_2(A[0][i], A[1][i], A[2][i], A[3][i]))
    res = max(res, check_2(A[0][0], A[1][1], A[2][2], A[3][3]))
    res = max(res, check_2(A[3][0], A[2][1], A[1][2], A[0][3]))
    return res

n = int(input())

for i in range(n):
    A = [0] * 4
    flag = 0

    for j in range(4):
        A[j] = input()
        
        if '.' in A[j]:
            flag = 1
    print('Case #' + str(i + 1) + ': ', end = '')
    
    if solve_X(A):
        print('X won')
    elif solve_O(A):
        print('O won')
    elif flag:
        print('Game has not completed')
    else:
        print('Draw')
    
    try:
        input()
    except:
        exit()
