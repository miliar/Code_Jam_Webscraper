# Standing Ovation

import fileinput

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
    n, s = f.readline().rstrip().split(' ')
    n = int(n)
    u, z = 0, 0
    for i, c in enumerate(map(int, s)):
        d = max(i - u, 0)
        u += d + c
        z += d
    print('Case #%d: %d' % (t + 1, z))
