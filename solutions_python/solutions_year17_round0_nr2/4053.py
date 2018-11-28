#tidy numbers
N = input()
for i in xrange(N):
    q = input()
    j = q
    while 1:
        if sorted(str(j)) == [x for x in str(j)]:
            print 'Case #' + str(i + 1) + ': ' + str(j)
            break
        j -= 1
    #print '?'
