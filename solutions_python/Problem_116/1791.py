f = open('A-large.in', 'r')
q = open('output', 'w')
x = f.readlines()

counter = 1
ticR = []
t = int(x[0])

for i in range(t):
    for j in range(4):
        ticR.append(x[counter])
        counter += 1
    check = 0
    for s in range(4):
        if (ticR[s][0] == "O" or ticR[s][0] == "T") and (ticR[s][1] == "O" or ticR[s][1] == "T") and (ticR[s][2] == "O" or ticR[s][2] == "T") and (ticR[s][3] == "O" or ticR[s][3] == "T"): 
            check = 2
            q.write("Case #" + str(i+1) + ": O won\n")
            break
        if (ticR[s][0] == "X" or ticR[s][0] == "T") and (ticR[s][1] == "X" or ticR[s][1] == "T") and (ticR[s][2] == "X" or ticR[s][2] == "T") and (ticR[s][3] == "X" or ticR[s][3] == "T"):
            check = 2
            q.write("Case #" + str(i+1) + ": X won\n")
            break
        if (ticR[0][s] == "O" or ticR[0][s] == "T") and (ticR[1][s] == "O" or ticR[1][s] == "T") and (ticR[2][s] == "O" or ticR[2][s] == "T") and (ticR[3][s] == "O" or ticR[3][s] == "T"):
            check = 2
            q.write("Case #" + str(i+1) + ": O won\n")
            break
        if (ticR[0][s] == "X" or ticR[0][s] == "T") and (ticR[1][s] == "X" or ticR[1][s] == "T") and (ticR[2][s] == "X" or ticR[2][s] == "T") and (ticR[3][s] == "X" or ticR[3][s] == "T"):
            check = 2
            q.write("Case #" + str(i+1) + ": X won\n")
            break
    if (ticR[0][0] == "O" or ticR[0][0] == "T") and (ticR[1][1] == "O" or ticR[1][1] == "T") and (ticR[2][2] == "O" or ticR[2][2] == "T") and (ticR[3][3] == "O" or ticR[3][3] == "T") and (check != 2):
        check = 4
        q.write("Case #" + str(i+1) + ": O won\n")
    if (ticR[0][0] == "X" or ticR[0][0] ==  "T") and (ticR[1][1] == "X" or ticR[1][1] == "T") and (ticR[2][2] == "X" or ticR[2][2] == "T") and (ticR[3][3] == "X" or ticR[3][3] == "T") and (check != 2):
        check = 4
        q.write("Case #" + str(i+1) + ": X won\n")
    if (ticR[3][0] == "O" or ticR[3][0] ==  "T") and (ticR[2][1] == "O" or ticR[2][1] == "T") and (ticR[1][2] == "O" or ticR[1][2] == "T") and (ticR[0][3] == "O" or ticR[0][3] == "T") and (check != 2):
        check = 4
        q.write("Case #" + str(i+1) + ": O won\n")
    if (ticR[3][0] == "X" or ticR[3][0] ==  "T") and (ticR[2][1] == "X" or ticR[2][1] == "T") and (ticR[1][2] == "X" or ticR[1][2] == "T") and (ticR[0][3] == "X" or ticR[0][3] == "T") and (check != 2):
        check = 4
        q.write("Case #" + str(i+1) + ": X won\n")
        
    for k in range(4):
        for m in range(4):
            if (ticR[k][m] == ".") and (check == 0):
                check = 2
                q.write("Case #" + str(i+1) + ": Game has not completed\n")
                break

    if check == 0:
        q.write("Case #" + str(i+1) + ": Draw\n")
    counter += 1
    ticR = []

f.close()
q.close()
print "Finished"
