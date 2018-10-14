f = open("A-large.in")
lines = f.readlines()

global case
case = 1


def feed(board, dotted, case):
    #check each row
    for each in board:
        verdict = check(each)
        if verdict == "O" or verdict == "X":
            print "Case #" + str(case) + ":", verdict, "won"
            return
    #check each column
    for i in range(4):
        each = []
        for j in range(4):
            each += board[j][i]
        verdict = check(each)
        if verdict == "O" or verdict == "X":
            print "Case #" + str(case) + ":", verdict, "won"
            return

    #check long diagonals
    diagonals = []
    diagonals += [[board[0][0],board[1][1],board[2][2],board[3][3]]]
    diagonals += [[board[0][3],board[1][2],board[2][1],board[3][0]]]
    for each in diagonals:
        verdict = check(each)
        if verdict == "O" or verdict == "X":
            print "Case #" + str(case) + ":", verdict, "won"
            return



    if dotted:
        print "Case #" + str(case) + ":","Game has not completed"
    else:
        print "Case #" + str(case) + ":", "Draw"
    

def check(l):
    #print l
    s = set(l)
    length = len(s)
    if length == 1 and (l[0] != "." and l[0] != "T"):
        #print "winner 1",l
        return l[0]
    elif length == 2 and "T" in s:
        #print "winner 2",l
        return sorted(l)[1]
    else:
        return "T"


cases = int(lines[0])
for i in range(1, len(lines), 5):
    board = []
    dotted = False
    for j in range(4):
        temp = list(lines[i+j])
        temp.remove("\n")
        if "." in temp:
            dotted = True
        board += [temp]
    feed(board, dotted, case)
    case +=1
print ""

