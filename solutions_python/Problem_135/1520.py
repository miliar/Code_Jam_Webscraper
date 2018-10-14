# https://code.google.com/codejam/contest/2974486/dashboard#s=p0
import sys

def readline():
    return sys.stdin.readline().rstrip()

def getrow(rownum):
    for i in range(4):
        line = readline()
        if (i+1) == rownum:
            nums = [int(s) for s in line.split()]
    return nums

t = int(readline())
for x in range(t):
    rownum = int(readline())
    nums1 = getrow(rownum)
    rownum = int(readline())
    nums2 = getrow(rownum)
    intersect = list(set(nums1) & set(nums2))
    if len(intersect) == 1:
        result = intersect[0]
    elif len(intersect) == 0:
        result = 'Volunteer cheated!'
    else:
        result = 'Bad magician!'
    print 'Case #{}: {}'.format(x+1, result)

