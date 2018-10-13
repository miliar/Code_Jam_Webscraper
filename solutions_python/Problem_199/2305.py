def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_output():
    lines = getInput("inputA.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        sol = get_solution(lines[case])
        print "Case #{0}: {1}".format(case, sol)
        case += 1


def get_solution(testcase):
    S, K = testcase.split(" ")
    S = list(S)
    K = int(K)
    count = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            count += 1
            flip(S, i, K)
        i += 1
    i = len(S) - K
    while i < len(S):
        if S[i] == '-':
            return 'IMPOSSIBLE'
        i += 1
    return count


def flip(S, i, K):
    for p in range(i + K):
        c = S[p]
        if c == '+':
            c = '-'
        else:
            c = '+'
        S[p] = c
        p += 1

print_output()
