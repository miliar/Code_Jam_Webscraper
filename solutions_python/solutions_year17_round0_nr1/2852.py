import sys
sys.stdin = open('A-large.in')
sys.stdout = open('A-large.out', 'w')

def flip(row, idx, size):
    for i in xrange(size):
        row[idx+i] = 1 - row[idx+i]
    return row
def solve():
    s,k = sys.stdin.readline().strip().split(' ')
    row = [[0,1][c=='+'] for c in s]
    k = int(k)
    l = len(row)

    flips = 0

    for i in xrange(l):
        if row[i] == 0 and i<=l-k:
            row = flip(row, i, k)
            flips += 1

    zeros = l - sum(row)

    if zeros:
        return 'IMPOSSIBLE'
    else:
        return flips

t = int(sys.stdin.readline())
for _t in xrange(t):
    print "Case #" + str(_t + 1) + ":", solve()

