#Tic-Tac-Toe-Tomek
start_of_case = True
i = 0
cases = []
incomplete_case = []
IN = open('A-large.txt','r')
for line in IN:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        if(len(line) > 1):
            if(start_of_case):
                temp_count = 0
                start_of_case = False
                temp_row = []
                temp_row.append(line[0])
                temp_row.append(line[1])
                temp_row.append(line[2])
                temp_row.append(line[3])
                temp_count += 1
                incomplete_case.append(temp_row)
            else:
                temp_row = []
                temp_row.append(line[0])
                temp_row.append(line[1])
                temp_row.append(line[2])
                temp_row.append(line[3])
                incomplete_case.append(temp_row)
                temp_count += 1
                if(temp_count >= 4):
                    start_of_case = True
                    cases.append(incomplete_case)
                    incomplete_case = []

i = 0
OUT = open('A-large-out.txt','w')
for x in cases:
    already_won = False
    outcome = ""
    i = i + 1
    #print x
    # Check rows
    for row in range(0,len(x)):
        if((x[row][0] == 'O' or x[row][0] == 'T') and
            (x[row][1] == 'O' or x[row][1] == 'T') and
            (x[row][2] == 'O' or x[row][2] == 'T') and
            (x[row][3] == 'O' or x[row][3] == 'T')):
            outcome = "O won"
            already_won = True

        elif((x[row][0] == 'X' or x[row][0] == 'T') and
            (x[row][1] == 'X' or x[row][1] == 'T') and
            (x[row][2] == 'X' or x[row][2] == 'T') and
            (x[row][3] == 'X' or x[row][3] == 'T')):
            outcome = "X won"
            already_won = True

    # Check cols
    for col in range(0,len(x)):
        if((x[0][col] == 'O' or x[0][col] == 'T') and
            (x[1][col] == 'O' or x[1][col] == 'T') and
            (x[2][col] == 'O' or x[2][col] == 'T') and
            (x[3][col] == 'O' or x[3][col] == 'T')):
            outcome = "O won"
            already_won = True

        elif((x[0][col] == 'X' or x[0][col] == 'T') and
            (x[1][col] == 'X' or x[1][col] == 'T') and
            (x[2][col] == 'X' or x[2][col] == 'T') and
            (x[3][col] == 'X' or x[3][col] == 'T')):
            outcome = "X won"
            already_won = True

    if((x[0][0] == 'O' or x[0][0] == 'T') and
        (x[1][1] == 'O' or x[1][1] == 'T') and
        (x[2][2] == 'O' or x[2][2] == 'T') and
        (x[3][3] == 'O' or x[3][3] == 'T')):
        outcome = "O won"
        already_won = True

    elif((x[0][0] == 'X' or x[0][0] == 'T') and
        (x[1][1] == 'X' or x[1][1] == 'T') and
        (x[2][2] == 'X' or x[2][2] == 'T') and
        (x[3][3] == 'X' or x[3][3] == 'T')):
        outcome = "X won"
        already_won = True

    if((x[0][3] == 'O' or x[0][3] == 'T') and
        (x[1][2] == 'O' or x[1][2] == 'T') and
        (x[2][1] == 'O' or x[2][1] == 'T') and
        (x[3][0] == 'O' or x[3][0] == 'T')):
        outcome = "O won"
        already_won = True

    elif((x[0][3] == 'X' or x[0][3] == 'T') and
        (x[1][2] == 'X' or x[1][2] == 'T') and
        (x[2][1] == 'X' or x[2][1] == 'T') and
        (x[3][0] == 'X' or x[3][0] == 'T')):
        outcome = "X won"
        already_won = True

    if(not already_won):
        stillgame = False
        for y in x:
            if ("." in y):
                stillgame = True
        if(not stillgame):
            outcome = "Draw"
        else:
            outcome = "Game has not completed"

    print "Case #{0}: {1}".format(i,outcome)
    OUT.write("Case #{0}: {1}\n".format(i,outcome))

OUT.close()

            
                
            
    
