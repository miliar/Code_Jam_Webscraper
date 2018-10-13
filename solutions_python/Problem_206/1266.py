def solve(d, horses):
    max = -1
    for k, s in horses:
        t = (d - k) / s
        if t > max:
            max = t
    sol = d / max
    return sol


solutions = []

with open('A-large.in') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        d, n = map(int, f.readline().split())
        horses = []
        for h in range(n):
            k, s = map(int, f.readline().split())
            horses.append((k, s))
        solutions.append(solve(d, horses))

with open('A-large-solution', 'w') as sol_file:
    for i, sol in enumerate(solutions):
        sol_file.write("Case #{}: {}\n".format(i + 1, sol))
