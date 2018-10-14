#!/usr/bin/env python

cseq = ((-1, 0), (0, -1), (0, 1), (1, 0))

MAX_INT = 0x7FFFFFFF

def refine(mx, nums, big, small, r):
#    print 'refine', nums, big, small, r
    for i in range(min(r, len(mx))):
        for j in range(len(mx[i])):
            if mx[i][j] == big:
                mx[i][j] = small
    nums.remove(big)

def get_basin(region, i, j):
    if i < 0 or j < 0:
        return MAX_INT
    elif i >= len(region) or j >= len(region[0]):
        return MAX_INT
    else:
        return region[i][j]


def read_map(fin, m):
    region = []
    for i in range(m):
        region.append([int(i) for i in fin.readline().split(' ')])
    return region

def solve_case(fin):
    m, n = [int(i) for i in fin.readline().split(' ')]
    region = read_map(fin, m)

    if m == 1 and n == 1:
        return [[1]], [1]

    nums = []
    lg = 1
    base = [0]*n
    mx = [base[:] for i in range(m)]
    for i in range(m):
        for j in range(n):
#            print 'i, j', i, j
            if mx[i][j] == 0:
                mx[i][j] = lg
                nums.append(lg)
#                print lg
                lg += 1

#            seqs = [(i+dx, y+dy) for (dx, dy) in cseq]
#            basins = [get_basin(region, x, y) for (x, y) in seqs]
#            pos, val = min(zip(range(4), basins), key=lambda x:x[1])
            val = MAX_INT
            x, y = 0, 0
            for k in cseq:
                newv = get_basin(region, i+k[0], j+k[1])
                if val > newv:
                    val = newv
                    x, y = i+k[0], j+k[1]

#            print 'x, y', x, y, val
#            print mx
            if val < region[i][j]:
#                print 'old', mx[x][y]
                if mx[x][y] == 0:
                    mx[x][y] = mx[i][j]
#                    print mx[x][y]
                elif mx[x][y] != mx[i][j]:
#                    print x, y, i, j
                    refine( mx, nums, max(mx[i][j], mx[x][y]), min(mx[i][j], mx[x][y]), i+2)

    return mx, nums


def printmx(matrix, nums):
#    print matrix, nums
    lables = [chr(ord('a') + i) for i in range(len(nums))]
    lmap = dict(zip(nums, lables))
    for l in matrix:
        print ' '.join([lmap[i] for i in l])

def solve(fin):
    n = int(fin.readline())
    for i in range(n):
        mx, nums = solve_case(fin)
        print 'Case #{0}:'.format(i+1)
        printmx(mx, nums)

def main():
    import sys
    solve(sys.stdin)

if __name__ == '__main__':
    main()
