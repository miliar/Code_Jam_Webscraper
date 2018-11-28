input = open("tttt.in" , "r")
output = open("tttt.out" , "w")
cases = int(input.readline())

for i in range(1, cases + 1):
    tttt = [list(input.readline())[0:-1], list(input.readline())[0:-1], list(input.readline())[0:-1], list(input.readline())[0:-1]]
    result = "undecided"
    for j in range(0, 4):
        if (((tttt[j][1] == tttt[j][0]) or (tttt[j][1] == "T")) and ((tttt[j][2] == tttt[j][0]) or (tttt[j][2] == "T")) and ((tttt[j][3] == tttt[j][0]) or (tttt[j][3] == "T"))) and (tttt[j][0] != "."):
            result = tttt[j][0] + " won"
        if (((tttt[1][j] == tttt[0][j]) or (tttt[1][j] == "T")) and ((tttt[2][j] == tttt[0][j]) or (tttt[2][j] == "T")) and ((tttt[3][j] == tttt[0][j]) or (tttt[3][j] == "T"))) and (tttt[0][j] != "."):
            result = tttt[0][j] + " won"
    for j in range(0, 2):
        if (((tttt[1][1] == tttt[0][0]) or (tttt[1][1] == "T")) and ((tttt[2][2] == tttt[0][0]) or (tttt[2][2] == "T")) and ((tttt[3][3] == tttt[0][0]) or (tttt[3][3] == "T"))) and (tttt[0][0] != "."):
            result = tttt[0][0] + " won"
        if (((tttt[1][2] == tttt[0][3]) or (tttt[1][2] == "T")) and ((tttt[2][1] == tttt[0][3]) or (tttt[2][1] == "T")) and ((tttt[3][0] == tttt[0][3]) or (tttt[3][0] == "T"))) and (tttt[0][3] != "."):
            result = tttt[0][3] + " won"
    if result == "undecided":
        if "." in [x for sublist in tttt for x in sublist]:
            result = "Game has not completed"
        else:
            result = "Draw"
    input.readline()
    print "Case #" + str(i) + ": " + result
    output.write("Case #" + str(i) + ": " + result + "\n")
input.close()
output.close()
