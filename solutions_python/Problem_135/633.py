import sys
sys.stdin = open('input', 'r')

def solve(a, na, b, nb):
    result = []
    for i in range(4):
        for j in range(4):
            if na[a - 1][i] == nb[b - 1][j]:
                result.append(na[a - 1][i])
                break
    if len(result) == 0:
        return 'Volunteer cheated!'
    elif len(result) > 1:
        return 'Bad magician!'
    else:
        return repr(result[0])

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases + 1):
    fr = int(sys.stdin.readline())
    first = []
    for i in range(4):
        first.append([int(n) for n in sys.stdin.readline().split()])
    sr = int(sys.stdin.readline())
    second = []
    for i in range(4):
        second.append([int(n) for n in sys.stdin.readline().split()])
    print 'Case #' + repr(casenum) + ': ' + solve(fr, first, sr, second)
