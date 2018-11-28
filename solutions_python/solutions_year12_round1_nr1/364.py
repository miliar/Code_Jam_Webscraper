import math

chars_typed = []
pass_length = []
prob_right = []
i = 0
IN = open('ASmallIn.txt','r')
OUT = open('ASmallOut.txt','w')
for line in IN:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        #DATA RETRIEVAL:
        if(math.fmod(i,2) == 0):
            data = line.split(' ')
            chars_typed.append(int(data[0]))
            pass_length.append(int(data[1]))
        else:
            data = line.split(' ')
            temp_prob = []
            for j in range(0, len(data)):
                temp_prob.append(float(data[j]))
            prob_right.append(temp_prob)        
            
print total_cases
print chars_typed
print pass_length
print prob_right

for i in range(0,total_cases):
    print "CASE #{0}".format(i+1)
    solution = 0
    prob_grid = []
    if(chars_typed[i] == 1):
        prob_grid.append(prob_right[i][0])
        prob_grid.append(1.0 - prob_right[i][0])
    elif(chars_typed[i] == 2):
        prob_grid.append(prob_right[i][0] * prob_right[i][1])
        prob_grid.append(prob_right[i][0] * (1.0 - prob_right[i][1]))
        prob_grid.append((1.0 - prob_right[i][0]) * prob_right[i][1])
        prob_grid.append((1.0 - prob_right[i][0]) * (1.0 - prob_right[i][1]))
    elif(chars_typed[i] == 3):
        prob_grid.append(prob_right[i][0] * prob_right[i][1] * prob_right[i][2])
        prob_grid.append(prob_right[i][0] * prob_right[i][1] * (1.0 - prob_right[i][2]))
        prob_grid.append(prob_right[i][0] * (1.0 - prob_right[i][1]) * prob_right[i][2])
        prob_grid.append(prob_right[i][0] * (1.0 - prob_right[i][1]) * (1.0 - prob_right[i][2]))
        prob_grid.append((1.0 - prob_right[i][0]) * prob_right[i][1] * prob_right[i][2])
        prob_grid.append((1.0 - prob_right[i][0]) * prob_right[i][1] * (1.0 - prob_right[i][2]))
        prob_grid.append((1.0 - prob_right[i][0]) * (1.0 - prob_right[i][1]) * prob_right[i][2])
        prob_grid.append((1.0 - prob_right[i][0]) * (1.0 - prob_right[i][1]) * (1.0 - prob_right[i][2]))
    #print prob_grid

    #EXPECTED KEYSTROKES IF KEEP TRYING
    strokes_if_correct = float(pass_length[i] - chars_typed[i] + 1)
    strokes_if_wrong = float(2 * (pass_length[i] + 1) - chars_typed[i])
    keep_trying = (prob_grid[0] * strokes_if_correct) + ((1.0 - prob_grid[0]) * strokes_if_wrong)
    print keep_trying

    #EXPECTED KEYSTROKES IF STARTOVER
    start_over = float(2.0 + pass_length[i])
    print start_over

    #DELETE ONE CHAR
    one_char = 0
    if(chars_typed[i] == 1):
        one_char = float(3 + pass_length[i] - chars_typed[i])
    elif(chars_typed[i] == 2):
        strokes_if_correct = float(pass_length[i] - chars_typed[i] + 3)
        strokes_if_wrong = float(pass_length[i] - chars_typed[i] + 4 + pass_length[i])
        one_char = (prob_grid[0]+prob_grid[1])*strokes_if_correct + (1.0 - (prob_grid[0]+prob_grid[1]))*strokes_if_wrong
    elif(chars_typed[i] == 3):
        strokes_if_correct = float(pass_length[i] - chars_typed[i] + 3)
        strokes_if_wrong = float(pass_length[i] - chars_typed[i] + 4 + pass_length[i])
        one_char = (prob_grid[0]+prob_grid[1])*strokes_if_correct + (1.0 - (prob_grid[0]+prob_grid[1]))*strokes_if_wrong
    print one_char

    #DELETE 2 CHAR
    two_char = 3*pass_length[i]
    if(chars_typed[i] == 2):
        two_char = float(5 + pass_length[i] - chars_typed[i])
    elif(chars_typed[i] == 3):
        strokes_if_correct = float(pass_length[i] - chars_typed[i] + 5)
        strokes_if_wrong = float(pass_length[i] - chars_typed[i] + 6 + pass_length[i])
        two_char = (prob_grid[0]+prob_grid[1]+prob_grid[2]+prob_grid[3])*strokes_if_correct + (1.0 - (prob_grid[0]+prob_grid[1]+prob_grid[2]+prob_grid[3]))*strokes_if_wrong
    print two_char

    #DELET 3 CHAR
    three_char = 3*pass_length[i]
    if(chars_typed[i] == 3):
        three_char = float(7 + pass_length[i] - chars_typed[i])

    solution = min(keep_trying, start_over, one_char, two_char, three_char)
    
    print("Case #{0}: {1}".format(i+1,solution))
    OUT.write("Case #{0}: {1}\n".format(i+1,solution))
OUT.close()
