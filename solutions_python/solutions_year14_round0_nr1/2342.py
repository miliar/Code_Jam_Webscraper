import sys

#def dbg(s): sys.stderr.write(str(s) + "\n")
def dbg(s): None
def reads(t): return list(map(t, input().split(" ")))
def read(t): return t(input())


def readAnswer():
    answer = read(int)
    board = []
    for i in range(0, 4):
        board.append(reads(int))

    return board[answer-1]

T = read(int)

for t in range(1, T+1):
    r1 = readAnswer()
    r2 = readAnswer()
    mc = 0
    cn = -1
    for i in range(0, 4):
        c = r1[i]
        if r2.count(c) > 0:
            mc += 1
            cn = c

    if mc == 1:
        s = cn
    elif mc > 1:
        s = "Bad magician!"
    elif mc == 0:
        s = "Volunteer cheated!"
    else:
        s = "ERROR"

    print("Case #%d: %s" % (t, s))
