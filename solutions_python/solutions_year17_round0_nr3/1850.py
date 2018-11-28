import sys

sys.stdin = open('C.in')

t = int(raw_input())

for i in xrange(t):
    temp = []
    n, k = map(int, raw_input().split())
    left = (n-1) - (n-1)/2
    right = (n-1)/2
    temp.append(left)
    temp.append(right)
    for j in xrange(k-1):
        #print temp
        left = (temp[0]-1) - (temp[0]-1)/2
        right = (temp[0]-1)/2
        temp.append(left)
        temp.append(right)
        temp.sort()
        temp.reverse()
        del temp[0]
    print 'Case #%d: %d %d' %(i+1, max(left, 0), max(right, 0))
