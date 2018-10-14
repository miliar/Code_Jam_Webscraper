import sys

cases = int(sys.stdin.readline())

for i in range(1,cases+1):
    r1 = int(sys.stdin.readline())
    board1 = []
    for j in range(4):
        board1.append(set(sys.stdin.readline().strip().split()))


    r2 = int(sys.stdin.readline())
    board2 = []
    for j in range(4):
        board2.append(set(sys.stdin.readline().strip().split()))

    solutions = board1[r1-1] & board2[r2-1]
    if len(solutions) == 0:
        print("Case #%s: Volunteer cheated!" % i)
    elif len(solutions) == 1:
        print("Case #%s: %s" % ( i, solutions.pop() ))
    else:
        print("Case #%s: Bad magician!" % i)
