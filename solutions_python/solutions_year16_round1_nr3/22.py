
import sys
from collections import Counter, defaultdict

debug = False

def cycles(p):
    d = dict(enumerate(p))
    nn = []
    while d:
        ring = []
        x = list(d)[0]
        while x not in ring and x in d:
            ring += [x]
            x = d.pop(x)

        if x in ring:
            cycle_length = len(ring) - ring.index(x)
            nn += [cycle_length]
    if debug: print nn
    return nn

def pointer_tree(p):
    ptrs = defaultdict(list)
    d = dict(enumerate(p))
    for k in list(d):
        ptrs[d[k]] += [k]
        
    return ptrs

def max_tree(a, ignore, ptrs):
    sources = list(ptrs[a])
    sources = [s for s in sources if s != ignore]
    if not sources:
        if debug: print a
        return 1
    tree_value = 1 + max(max_tree(s, None, ptrs) for s in sources)
    if debug: print a, ignore, sources, '->', tree_value
    return tree_value

def trees(p):
    d = dict(enumerate(p))
    nn = []
    for k in range(len(p)):
        if d[d[k]] == k:
            # this is a pair
            nn += [(k, d[k])]

    # now nn is double counted.
    ptrs = pointer_tree(p)
    nn = [(l,r) for (l,r) in nn if l < r]

    if debug: print 'pairs', nn

    lens = []
    for (a,b) in nn:
        lens += [max_tree(a, b, ptrs) + max_tree(b, a, ptrs)]

    if debug: print lens
    return lens
    
def bffs(values):
    max_cycle = max(cycles(values))
    if debug: print max_cycle
    all_trees = sum(trees(values))
    return max(max_cycle, all_trees)

def main():
    t = int(sys.stdin.readline().strip())
    for k in range(t):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        values = map(int, line.split())
        values = [v-1 for v in values]
        solution = bffs(values)
        print 'Case #' + str(k+1) + ': ' + str(solution)

if __name__ == '__main__':
    main()

