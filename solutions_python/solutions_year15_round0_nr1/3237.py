def solve(n, l):
    count = 0
    ans = 0
    for i in xrange(n):
        count += l[i]
        while (count <= i):
            ans += 1
            count += 1
        #print "count = %d, ans = %d" % (count, ans,)
    return ans

T = input()
for i in xrange(T):
    print 'Case #%d:' % (i + 1),
    (s_max, input_list) = raw_input().split()
    input_list = map(int, list(input_list))
    #print s_max
    #print input_list
    ans = solve(int(s_max), input_list)
    print ans
    #print "the answer is %d" % (ans,)
