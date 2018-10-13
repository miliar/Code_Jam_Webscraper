import fileinput

e = 0
remaining = 0
for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    if not remaining:
        e += 1
        N, Q = line.strip().split()
        N = int(N)
        remaining = N * 2 + 1
        ns = []
        ds = []
    elif remaining > N + 1:
        K, S = line.strip().split()
        K = int(K)
        S = int(S)
        ns.append((K, S))
        remaining -= 1
    elif remaining > 1:
        d = [int(c) for c in line.strip().split() if int(c) != -1]
        if d:
            ds.append(d[0])
        remaining -= 1
    else:
        remaining -= 1
    if not remaining:

        #print("ns", ns)
        endurance, speed = ns[0][0], ns[0][1]
        solutions = [[ds[0] / speed, endurance - ds[0], speed]]
        #print(solutions)
        best = solutions[0][0]

        for i in range(1, len(ns) - 1):
            new_solutions = []
            distance = ds[i]
            for s in solutions:
                #print("hm", s)
                if s[1] >= distance:
                    new_solutions.append([s[0] + distance / s[2], s[1] - distance, s[2]])
            if ns[i][0] >= distance:
                new_solutions.append([best + distance / ns[i][1], ns[i][0] - distance, ns[i][1]])
            solutions = new_solutions
            solutions.sort()
            best = solutions[0][0]
            #print("sols", solutions)

        print("Case #{}: {}".format(e, best))
