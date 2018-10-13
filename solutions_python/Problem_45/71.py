import sys
import itertools

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xpermutations(items):
    return xcombinations(items, len(items))

def calc_coins(cell, release_order):
    if len(release_order) == 0:
        return 0
    idx = release_order[0]
    cell = list(cell)
    cell[idx] = 0
    coin = 0
    for i in range(idx+1, len(cell)):
        if cell[i] == 0:
            break
        coin = coin + 1
    for i in range(idx-1, 0, -1):
        if cell[i] == 0:
            break
        coin = coin + 1

    return coin + calc_coins(cell, release_order[1:])
    

T = int(sys.stdin.readline())

for i in range(T):
    line = sys.stdin.readline()
    P = int(line.split()[0])
    Q = int(line.split()[1])

    cell = [0] + [1 for x in range(P)]

    cell_to_release = [int(x) for x in sys.stdin.readline().split()]

    mincoin = 1234567890
    for perm in xpermutations(cell_to_release):
        coin = calc_coins(cell, perm)
        if mincoin > coin:
            mincoin = coin

    print "Case #%d: %d"%(i+1, mincoin)
        
