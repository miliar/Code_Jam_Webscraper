def Tic_tac():
    X_win = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
    O_win = ['OOOO', 'OOOT', 'OOTO', 'OTOOO', 'TOOO']
    for i in range(0,number_of_cases):
        output_file.write('Case #'+ str(i+1)+': ')
        input_lines = [inputs[5*i+1].split('\n')[0], inputs[5*i+2].split('\n')[0], inputs[5*i+3].split('\n')[0], inputs[5*i+4].split('\n')[0]]
        count = 0
        flag = 0
        for j in range(0,4):
            if '.' not in input_lines[j]:
                count+=1
                if input_lines[j] in X_win:
                    output_file.write('X won')
                    flag = 1
                    break
                elif input_lines[j] in O_win:
                    output_file.write('O won')
                    flag = 1
                    break

            check_line = input_lines[0][j] + input_lines[1][j] +input_lines[2][j] + input_lines[3][j]
            if '.' not in check_line:
                if check_line in X_win:
                    output_file.write('X won')
                    flag = 1
                    break
                elif check_line in O_win:
                    output_file.write('O won')
                    flag = 1
                    break
                
        if (flag != 1):
            check_line = input_lines[0][0] + input_lines[1][1] +input_lines[2][2] + input_lines[3][3]
            if check_line in X_win:
                output_file.write('X won')
                flag = 1
            elif check_line in O_win:
                output_file.write('O won')
                flag = 1
            if (flag!=1):
                check_line = input_lines[0][3] + input_lines[1][2] +input_lines[2][1] + input_lines[3][0]
                if check_line in X_win:
                    output_file.write('X won')
                    flag = 1
                elif check_line in O_win:
                    output_file.write('O won')
                    flag = 1
                    
            if (count == 4 and flag != 1):
                output_file.write('Draw')
            elif (flag != 1):
                output_file.write('Game has not completed')
        output_file.write('\n')

            
my_file = open('A-small-attempt0.in','r')
inputs = my_file.readlines()
my_file.close()
output_file = open('Aoutput1.out','w')
number_of_cases = int(inputs[0])
Tic_tac()
output_file.close()
