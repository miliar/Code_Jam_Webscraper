with open("A-large.in") as f:
    with open("output.txt", "w") as g:
        t = int(f.readline().strip())
        for i in range(1, t + 1):
            [d, n] = map(int, f.readline().split())
            max_time = 0
            for j in range(n):
                # work out how long it takes horse N to get to D
                [k, s] = map(int, f.readline().split())
                t = (d-k)/s
                if t > max_time:
                    max_time = t
            g.write("Case #{}: {}\n".format(i, d/max_time))
