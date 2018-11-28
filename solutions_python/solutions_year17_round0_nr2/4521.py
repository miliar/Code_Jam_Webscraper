def is_tidy(n):
    number = [int(d) for d in str(n)]
    for i in xrange(len(number) - 1):
        if number[i + 1] < number[i]:
	    return False
    return True

cases = int(raw_input())
for case in xrange(1, cases + 1):
    n = int(raw_input())
    
    while not is_tidy(n):
        n = n - 1
    print "Case #%d: %d" % (case, n)

