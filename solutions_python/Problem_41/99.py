import sys

# Find smallest digit in l > num
def findBigger(num, l):
    for i in range(num+1, 10):
        if i in l:
            return i

def solve(num):
    s = [int(d) for d in str(num)]
    # Look for digit from right till found bigger to its right.
    for i in range(len(s)-1, 0, -1):
        val = s[i-1]
        if val < max(s[i:]):
            right = s[i:]
            bigger = findBigger(val, right)
            s[i-1] = bigger
            right[right.index(bigger)] = val
            right.sort()
            s[i:] = right
            return int(''.join([str(d) for d in s]))
    if num < 10:
        return num*10
    bigger = findBigger(0, s)
    val = s[0]
    s[0] = bigger
    right = s[1:]
    if bigger not in right:
        return num * 10
    right[right.index(bigger)] = val
    right.sort()
    s[1] = 0
    s[2:] = right
    return int(''.join([str(d) for d in s]))

file = open(sys.argv[1])
numCases = int(file.readline())
for case in range(1, numCases+1):
    num = int(file.readline())
    val = solve(num)
    print 'Case #%d: %s' % (case, val)
