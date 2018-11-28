def solve(c, f, x):
    cps = 2.
    time = 0.

    while True:
        if x / (cps + f) < (x - c) / cps:
            time += c / cps
            cps += f
        else:
            time += x / cps
            break

    return time

f = open('B-large.in', 'r')
fo = open('B-large.out', 'w')

t = int(f.readline())
for ti in range(1, t + 1):
    data = [float(di) for di in f.readline().rstrip().split()]
    ans = 'Case #' + str(ti) + ': ' + str(solve(data[0], data[1], data[2]))
    fo.write(ans + '\n')

f.close()
fo.close()