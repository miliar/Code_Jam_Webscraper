def solve(V, X, pipes):
    if all(p[1] > X for p in pipes):
        return 'IMPOSSIBLE'
    if all(p[1] < X for p in pipes):
        return 'IMPOSSIBLE'

    if all(p[1] == X for p in pipes):
        return V / (sum(p[0] for p in pipes))

    total_diff = abs(X - pipes[0][1]) + abs(X - pipes[1][1])

    # print 'pipes', pipes
    # print 'total', total_diff
    v2 = abs(X - pipes[0][1]) / total_diff * V
    v1 = V - v2
    # print v1, v2
    return max(v1 / pipes[0][0], v2 / pipes[1][0])
    # return 0

input_file = open('b-small.in')
cases = int(input_file.readline().strip())
case = 0
while case < cases:
    case += 1
    N, V, X = [float(x) for x in input_file.readline().split()]
    N = int(N)
    pipes = []
    for i in range(N):
        pipes.append([float(x) for x in input_file.readline().strip().split()])

    print "Case #{}: {}".format(case, solve(V, X, pipes))
