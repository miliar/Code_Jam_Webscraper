for case in range(input()):
    number = map(int, raw_input())
    l = len(number)
    if l == 1:
    	print 'Case #%s: %s' % (case + 1, str(number[0]) + '0')
    	continue
    p = l - 1
    while p > 0 and int(number[p - 1]) >= int(number[p]):
    	p -= 1
    if (p == l - 1) and (l > 2 or number[l - 1] > 0):
    	t = number[p - 1]
    	number[p - 1] = number[p]
    	number[p] = t
    elif p > 0:
    	min_next = 10
    	next_pos = 0
    	for i in xrange(p, l):
    		if number[i] < min_next and number[i] > number[p - 1]:
    			min_next = number[i]
    			next_pos = i
    	number[next_pos] = number[p - 1]
    	number[p - 1] = min_next
    	number = number[0 : p] + sorted(number[p : ])
    else:
    	min_next = 10
    	next_pos = 0
    	for i in xrange(l):
    		if number[i] < min_next and number[i] > 0:
    			min_next = number[i]
    			next_pos = i
    	number[next_pos] = 0
    	number = [min_next] + sorted(number)	
    ans = ''.join(map(str, number))    
    print 'Case #%s: %s' % (case + 1, ans)
