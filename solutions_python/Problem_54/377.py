import sys

def solve(times):
    N = len(times)
    mintime = min(times)
    maxtime = max(times)
    T = maxtime - mintime
    for t in times:
        if t != mintime:
            T = min(t - mintime, T)

    def T_test(T):
        for t1 in times:
            for t2 in times:
                diff = abs(t1 - t2)
                rest = diff % T
                if rest != 0:
                    return rest
        return T

    while True:
        T2 = T_test(T)
        if T == T2:
            break
        else:
            T = T2

    y = 0
    for t in times:
        rest = t % T
        if rest != 0:
            y = max(T - rest, y)

    def y_test(y):
        for t in times:
            if (t + y) % T != 0:
                print "False"
                return False
        return True

    while not y_test(y):
        y += T

    return y


C = input()
for c in range(C):
    sys.stderr.write("c: %d\n" % c)
    line = raw_input().split(' ')
    N = int(line[0])
    times = []
    for n in range(N):
        times.append(int(line[n+1]))
    print "Case #%d: %d" % (c+1, solve(times))


        
