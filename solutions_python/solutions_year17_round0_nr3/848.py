import bisect

def tree(n, k):
    base = 1
    while k - base*2 >= 0:
        base *= 2
    d = k - base
    n = (n - d) // base
    return '%d %d' % (n//2, (n-1)//2)

lines = [l.split() for l in open('input')]
N = int(lines[0][0])
for i in range(N):
    print('Case #%d: %s' % (i+1, tree(int(lines[i+1][0]), int(lines[i+1][1]))))

