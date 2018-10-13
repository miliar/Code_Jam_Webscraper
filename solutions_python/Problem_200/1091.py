import sys

fp = open(sys.argv[1])
N = int(fp.readline().strip())

def foo(line):
    v = [int(x) for x in line]
    N = len(v)
    pos = N - 1
    while pos > 0:
        if v[pos] < v[pos - 1]:
            k = pos
            while k < N:
                v[k] = 9
                k += 1
            v[pos - 1] = v[pos - 1] - 1
        pos -= 1
    return str(int(''.join([str(x) for x in v])))

for case in range(N):
    print 'Case #%d: %s' % (case + 1, foo(fp.readline().strip()))
fp.close()

