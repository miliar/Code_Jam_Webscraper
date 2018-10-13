import math

fin = open('A-small-attempt0.in', 'r')
fout = open('ass1.out', 'w')

N = int(fin.readline())

for n in range(N):
    r, t = map(float, fin.readline().split())
    cnt = 0

    while True:
        nr = r + 1.0
        s = 2.0 * r + 1.0
        t -= s
        if t < 0.0:
            break
        cnt += 1
        r += 2.0
    fout.write('Case #%i: %i\n' % (n + 1, cnt))