def solve(D, horses):
    solution = None
    for kilometer, speed in horses:
        left_to_travel = D - kilometer
        time_to_reach = left_to_travel / speed
        max_speed = D / time_to_reach
        if solution is None:
            solution = max_speed
        else:
            solution = min(solution, max_speed)

    return solution

if __name__ == '__main__':
    lines = open('A-large.in', 'r').readlines()
    test_cases = int(lines[0])
    T = 0
    line = 0
    while line + 1 < len(lines):
        line += 1
        D, N = lines[line].split()
        D, N = float(D), int(N)
        horses = []
        for j in xrange(N):
            line += 1
            K, S = lines[line].split()
            horses.append((float(K), float(S)))

        T += 1
        print 'Case #{0}: {1}'.format(T, solve(D, horses))