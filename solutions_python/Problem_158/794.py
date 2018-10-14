import math

input_file = open("D-small-attempt1.in")
output_file = open("ominous_omino.txt", 'w')
Testcases = int(input_file.readline()[:-1])
R = "RICHARD"
G = "GABRIEL"

def X_R_C_calc(string):
    '''
    returns the number of pancakes on each diner's plate
    '''
    string += ' '
    start = 0
    listy = []
    length = len(string)
    for index in range(length):
        if string[index] == ' ':
            listy.append(int(string[start:index]))
            start = index + 1
    return listy

def omino(listy):
    """
    decides the winner of the game
    """
    if listy[0] > 6:
        return R
    if (listy[1] * listy[2]) % listy[0] != 0:
        return R
    if listy[1] < listy[0] and listy[2] < listy[0]:
        return R
    if listy[1] >= listy[0] and listy[2] >= listy[0]:
        return G
    if listy[0] > 3 and (math.ceil(math.sqrt(listy[0])) >= listy[1] or math.ceil(math.sqrt(listy[0])) >= listy[2]):
        return R
    if listy[0] == 3 and (listy[1] == 1 or listy[2] == 1):
        return R
    return G

#main body of the program 
for test in range(Testcases):
    current_omino = input_file.readline()
    if current_omino[-1] == '\n':
        current_omino = current_omino[:-1]
    output_string = "Case #" + str(test + 1) + ": " + omino(X_R_C_calc(current_omino)) + '\n'
    output_file.write(output_string)

input_file.close()
output_file.close()
