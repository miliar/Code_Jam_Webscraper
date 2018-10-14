def process(num):
    start = 1
    smallest = start
    strnum = str(num)
    while start <= num:
        start = int(str(start) + '1')
        if start <= num:
            smallest = start
    smallest = str(smallest)
    small = smallest[:]
    l = len(smallest)
    for k in xrange(l):
        p1, p2 = smallest[:k], int(small[k:])
        p4 = int(strnum[k:])
        y = 2
        for y in xrange(y, 10):
            start = int(p1 + str(y*p2))
            if start > num:
                break
            else:
                smallest = str(start)
    return smallest

n = int(raw_input())
for i in xrange(n):
    print 'Case #' + str(i+1) + ':', process(int(raw_input()))

'''
4
111
1000
7
111111111111111110
'''