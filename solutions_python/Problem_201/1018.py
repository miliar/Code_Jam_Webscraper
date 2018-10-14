import math

input_name = 'C-small-2-attempt0.in'
output_name = 'small2-output'


input = open(input_name, 'r')
output = open(output_name, 'w')


def getInfos(N):
    if N % 2 == 0:
        maxS = N / 2
        minS = max(N / 2 - 1, 0)
    else:
        maxS = (N - 1) / 2
        minS = maxS
    return max(maxS, 0), max(minS, 0)


def getNext(K):
    l = math.floor(math.log(K, 2))
    p = 2 ** l
    if K < p + p / 2:
        return K - p / 2, 0
    else:
        return K - p, 1


def solve_better(N, K):
    if K == 1:
        return getInfos(N)
    else:
        a, b = getNext(K)
        n = solve_better(N, a)[b]
        return getInfos(n)


case = 0
for line in input:
    if case == 0:
        T = int(line)
    else:
        N, K = line.split(' ')
        N = int(N)
        K = int(K)
        sol1, sol2 = solve_better(N, K)
        output.write("Case #" + str(case) + ": " + str(sol1) + " " + str(sol2) + "\n")
    case += 1

input.close()
output.close()
