def pancake(s, k):
    if len(s) == k:
        if all([i=='+' for i in s]):
            return 0
        if all([i=='-' for i in s]):
            return 1
        return -99999
    if s[-1] == '-':
        for i in range(-k, 0):
            s[i] = {'+':'-', '-':'+'}[s[i]]
        return 1 + pancake(s[:-1], k)
    return pancake(s[:-1], k)

import sys
sys.setrecursionlimit(10000) 
if __name__ == "__main__":
    tests = open(sys.argv[1]).readlines()[1:]
    count = 1
    for t in tests:
        s, k =  t.strip().split(' ')
        s = list(s)
        k = int(k)
        p = pancake(s, k)
        if p >= 0:
            print "Case #%d: %d" % (count, p)
        else:
            print "Case #%d: IMPOSSIBLE" % (count)
        count += 1
