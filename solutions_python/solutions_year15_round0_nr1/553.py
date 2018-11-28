import sys, os, pdb

sys.setrecursionlimit(5000)

#infile = open('input')
infile = sys.stdin

def read_array(vtype):
    line = infile.readline()
    return [vtype(v) for v in line.split(' ')]

def solve(arr):
    ret = 0
    cur = 0
    for need, count in enumerate(arr):
        if count > 0:
            if need > cur:
                ret += need - cur
                cur += need - cur
            cur += count
    return ret

if __name__ == '__main__':
    T = int(infile.readline())
    for case in xrange(T):
        line = infile.readline()
        level, line = line.split(' ')
        line = line.strip()
        arr = [0] * len(line)
        for i, v in enumerate(line):
            arr[i] = int(v)
        ans = solve(arr)
        print 'Case #%d: %d' % (case + 1, ans)
            
            
