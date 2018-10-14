'''
Created on Apr 13, 2013

@author: Federico
'''
lst_number = [line.strip() for line in open('A-large.in', "r")]
file_solution = open('result.txt', 'w')

number_test = int(lst_number.pop(0))

for i in range(number_test):
    array = []
    for j in range(5):
        if j < 4:
            array.append(list(lst_number.pop(0)))
        else:
            if len(lst_number) > 0:
                lst_number.pop(0)

    empty = False
    found = False

    for index in range(4):
        if array[index].count('.') != 0:
            empty = True
        elif (array[index].count('X') == 3 and array[index].count('T') == 1) or array[index].count('X') == 4:
            string_result = "Case #%d: X won"%(i+1)
            found = True
        elif (array[index].count('O') == 3 and array[index].count('T') == 1) or array[index].count('O') == 4:
            string_result = "Case #%d: O won"%(i+1)
            found = True

        column = [array[0][index], array[1][index], array[2][index], array[3][index]]
        if (column.count('X') == 3 and column.count('T') == 1) or column.count('X') == 4:
            found = True
            string_result = "Case #%d: X won"%(i+1)
        elif (column.count('O') == 3 and column.count('T') == 1) or column.count('O') == 4:
            found = True
            string_result = "Case #%d: O won"%(i+1)

    diag1 = [array[0][0], array[1][1], array[2][2], array[3][3]]
    if (diag1.count('X') == 3 and diag1.count('T') == 1) or diag1.count('X') == 4:
            found = True
            string_result = "Case #%d: X won"%(i+1)
    elif (diag1.count('O') == 3 and diag1.count('T') == 1) or diag1.count('O') == 4:
            found = True
            string_result = "Case #%d: O won"%(i+1)

    diag2 = [array[0][3], array[1][2], array[2][1], array[3][0]]
    if (diag2.count('X') == 3 and diag2.count('T') == 1) or diag2.count('X') == 4:
            found = True
            string_result = "Case #%d: X won"%(i+1)
    elif (diag2.count('O') == 3 and diag2.count('T') == 1) or diag2.count('O') == 4:
            found = True
            string_result = "Case #%d: O won"%(i+1)
    
    if empty == False and found == False:
        string_result = "Case #%d: Draw"%(i+1)
    elif empty == True and found == False:
        string_result = "Case #%d: Game has not completed"%(i+1)
    
    print string_result
    file_solution.write(string_result + "\n")
