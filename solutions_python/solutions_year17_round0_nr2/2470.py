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


def get_solution(N):
    N = list(N.strip())
    N = map(int, N)
    for k in range(len(N)):
        for i in range(len(N) - 1):
            if N[i] > N[i+1]:
                N[i] -= 1
                i += 1
                while i < len(N):
                    N[i] = 9
                    i += 1
                break
    zeroes = True
    result = []
    for i in range(len(N)):
        if N[i] != 0:
            zeroes = False
        if not zeroes:
            result.append(N[i])
    return "".join(map(str, result))


print_output()
