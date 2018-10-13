import numpy as np

def my_trans(s, T):
    result = []
    exist_T = False
    exist_dot = False
    for i in s:
        if i == 'O':
            result.append(1)
        elif i == 'X':
            result.append(-1)
        elif i == '.':
            exist_dot = True
            result.append(0)
        elif i == 'T':
            exist_T = True
            result.append(T)
    return result, exist_T, exist_dot
        
if __name__ == '__main__':
    input_file = open('A-large.in', 'r')    
    T = int(input_file.readline().strip('\n'))

    output_list = []
    result = []

    for t in range(T):
        board_O = np.zeros([4, 4], int)
        board_X = np.zeros([4, 4], int)
        exist_T = False
        exist_dot = False
        row = []
        for i in range(4):            
            row.append(input_file.readline().strip('\n'))
            board_O[i, :], temp_T, temp_dot = my_trans(row[-1], T=1)
            if temp_T:
                exist_T = True
            if temp_dot:
                exist_dot = True
        # print('row: ', row)
        for i in range(4):
            if exist_T:
                board_X[i, :] = my_trans(row[i], T=-1)[0]
            else:
                board_X[i, :] = board_O[i, :]
            
        O_4 = board_O.sum(axis=0).max() == 4 or \
              board_O.sum(axis=1).max() == 4 or \
              np.trace(board_O) == 4 or \
              (board_O[0, 3] + board_O[1, 2] + \
              board_O[2, 1] + board_O[3, 0]) == 4        
        X_4 = board_X.sum(axis=0).min() == -4 or \
              board_X.sum(axis=1).min() == -4 or \
              np.trace(board_X) == -4 or \
              (board_X[0, 3] + board_X[1, 2] + \
              board_X[2, 1] + board_X[3, 0]) == -4
        # print(board_O)
        # print(board_X)
        # print('T ', exist_T, '. ', exist_dot, 'O ', O_4, 'X ', X_4)
        if O_4:
            if X_4:
                result.append('Draw')
            else:
                result.append('O won')
        else:
            if X_4:
                result.append('X won')
            else:
                if exist_dot:
                    result.append('Game has not completed')
                else:
                    result.append('Draw')        
        
        input_file.readline()
    
    input_file.close()

    # print(result)
    
    ans = open('ans.txt', 'w')
    i = 1
    while i <= T:
        ans.write('Case #' + str(i) + ': ' + result[i-1] + '\n')
        i = i + 1
    ans.close()

