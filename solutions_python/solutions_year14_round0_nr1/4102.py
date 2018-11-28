import sys


def solve_case(f):
    ans1 = int(f.readline().strip())

    board1 = []
    for n in range(4):
        board1.append(map(int, f.readline().strip().split()))

    row1 = set(board1[ans1 - 1])

    ans2 = int(f.readline().strip())
    board2 = []
    for n in range(4):
        board2.append(map(int, f.readline().strip().split()))
    row2 = set(board2[ans2 - 1])

    # Check if value is possible.
    x = row1 & row2
    
    if len(x) == 1:
        return x.pop()
    elif len(x) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


filename = sys.argv[1]
f = open(filename, 'r')
T = int(f.readline().strip())


for case in range(T):
    answer = solve_case(f)
    print "Case #%s: %s" % (case + 1, answer)
