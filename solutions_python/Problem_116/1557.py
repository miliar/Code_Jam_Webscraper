import sys

input_file=None
output_file=open("output.txt", 'w')
position_t=[-1,-2]
result_out=-1
            
    
def processBoard (board):
    global position_t
    col_result_array = [0,0,0,0]
    row_result_array=[0,0,0,0]
    diag_result_array=[0,0]
                    #R0, R1, R2, R3,C0 - C3, D1, D2
    dot_count=0
    row_sum=0
    for x in range(0,4):
        for y in range(0,4):
            if (board[x][y] == 'X'):
                col_result_array[y] += 1
                row_result_array[x] += 1
                if(x==y):
                    diag_result_array[0] += 1
                elif((x+y) == 3):
                    diag_result_array[1] += 1
            elif (board[x][y] == 'O'):
                col_result_array[y] -= 1
                row_result_array[x] -= 1
                if(x==y):
                    diag_result_array[0] -= 1
                elif((x+y) == 3):
                    diag_result_array[1] -= 1
            elif (board[x][y] == 'T'):
                position_t=[x,y]
            elif (board[x][y] == '.'):
                dot_count += 1
                

    for i in range(0,4):
        if((col_result_array[i] == 4) or (row_result_array[i] == 4)):
            output_file.write("X won\n")
            return
        elif((col_result_array[i] == -4) or (row_result_array[i] == -4)):
            output_file.write("O won\n")
            return
        elif((row_result_array[i] == -3) or (row_result_array[i] == 3) and (position_t[0]==i)):
            if(row_result_array[i] == -3):
                output_file.write("O won\n")
                return
            else :
                output_file.write("X won\n")
                return
        elif((col_result_array[i] == -3) or (col_result_array[i] == 3) and (position_t[1]==i)):
            if(col_result_array[i] == -3):
                output_file.write("O won\n")
                return
            else :
                output_file.write("X won\n")
                return
                
    #no result found in rows or coloumns
    #check diagonals
    if(diag_result_array[0]==4 or diag_result_array[1] == 4):
        output_file.write("X won\n")
        return
    elif(diag_result_array[0]==-4 or diag_result_array[1] == -4):
        output_file.write("O won\n")
        return
    elif(((diag_result_array[0] == 3) or (diag_result_array[1] == 3)) and ((position_t[0]==position_t[1]) or (position_t[0]+position_t[1] == 3))):
        output_file.write("O won\n")
        return
    elif(((diag_result_array[0] == -3) or (diag_result_array[1] == -3)) and ((position_t[0]==position_t[1]) or (position_t[0]+position_t[1] == 3))):
        output_file.write("O won\n")
        return
    if(dot_count > 0):
        output_file.write("Game has not completed\n")
    else:
        output_file.write("Draw\n")
def main():
    input_file=open(sys.argv[1], 'r')
    number_of_test_cases = int(input_file.readline())
    board = ["","","",""]
    for i in range (0,number_of_test_cases):
        output_file.write("Case #%d: " %(i+1))
        for j in range(0,4):
            board[j] = input_file.readline()
        input_file.readline()
        processBoard(board)
    return

main()