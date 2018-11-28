import sys, os, pdb

sys.setrecursionlimit(5000)

#infile = open('input')
infile = sys.stdin

def read_array(vtype):
    line = infile.readline()
    return [vtype(v) for v in line.split(' ')]

def get_time(pancakes, idx):
    if idx == 1:
        return 1
    if pancakes[idx] == 0:
        return get_time(pancakes, idx-1)

    count = pancakes[idx]
    if idx % 2 == 0:
        pancakes[idx / 2] += (2 * count)
    else:
        pancakes[idx / 2] += count
        pancakes[idx / 2 + 1] += count

    return min(idx, count + get_time(pancakes, idx-1))

def solve(arr):
    max_height = max(arr)
    ret = 1000
    for height in xrange(1, max_height + 1):
        cur = height
        for h in arr:
            cur += h / height
            if h % height == 0:
                cur -= 1
        ret = min(ret, cur)
    return ret

if __name__ == '__main__':
    T = int(infile.readline())
    for case in xrange(T):
        D = int(infile.readline())
        arr = read_array(int)
        ans = solve(arr)
        print 'Case #%d: %d' % (case + 1, ans)
            
            
