f = open('C-small-1-attempt0.in')
fw = open('C-small-1.out', 'w')

T = int(f.readline())
for t in xrange(T):
    N, K = map(int, f.readline().split())
    U = float(f.readline())
    cores = map(float, f.readline().split())
    cores.sort()
    imp = 0
    current = 0
    U_left = True
    while imp < N:
        target = cores[imp]
        improve = (target - current) * imp
        if U >= improve:
            U -= improve
            current = target
        else:
            current += U / imp
            U = 0
            U_left = False
            break
        imp += 1
    if U_left:
        improve = (1 - current) * N
        if U > improve:
            U -= improve
            current = 1
            imp = N
        else:
            current += U / imp
            U = 0
            imp = N
    prop = current ** imp
    for i in xrange(imp, N):
        prop *= cores[i]
    fw.write('Case #' + str(t + 1) + ': ' + '{0:.10f}'.format(prop) + '\n')

fw.close()
f.close()
