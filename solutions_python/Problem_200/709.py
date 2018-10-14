#intog

def tidy(n, prev, index, go_low):
	if n[index] == '0' and not go_low:
		return False, None
	if len(n)-1 == index:
		if go_low: 
		#	if n[index] == '0': return True, ''
			#else: return True, '9'
			return True, '9'
		if int(n[index]) >= prev:
			return True, n[index]
		return False, None
	k = int(n[index])
	if go_low:
		for i in xrange(9, prev-1, -1):
			if i < prev: break
			t, a = tidy(n, i, index+1, True)
			if t: return True, str(i)+a	
	else:
		if k >= prev:
			t, a = tidy(n, k, index+1, False)
			if t: return True, str(k)+a	
		for i in xrange(k-1, prev-1, -1):
			if i < prev: break
			t, a = tidy(n, i, index+1, True)
			if i==0 and index == 0:
				return True, a
			if t: return True, str(i)+a
	return False, None	

t = int(raw_input())
for i in xrange(t):
	n = raw_input()
	t, a = tidy(n,0,0,False)
	print "Case #{0}: {1}".format(i+1, a)
