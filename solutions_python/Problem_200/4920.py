def check_tidy(n):
	s = str(n)
	l = [ int(i) for i in s ]
	k = l[:]
	l.sort()
	if l == k:
		return True	
	else:
		return False
n = int(raw_input())
l = [ int(raw_input()) for  i in xrange(n) ]
result = []
for i in l:
	while(i>0):
		if(check_tidy(i)):
			result.append(i)
			break;
		else:
			i = i-1
for i in xrange(len(result)) : print "Case #{0}: {1}".format(i+1,result[i])
				



