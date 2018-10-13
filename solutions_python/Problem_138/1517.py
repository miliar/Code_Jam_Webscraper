def stairs(Na, Ke):
	key_Na = []
	key_Ke = []
	for i in range(n):
		key_Na.append('N')
		key_Ke.append('K')
        dict_Na = dict(zip(Na, key_Na))
        dict_Ke = dict(zip(Ke, key_Ke))
	dict_both = dict(dict_Na, **dict_Ke)
	value = []
	for k in sorted(dict_both.keys()):
		value.append(dict_both[k])
	return value

def deceit(n, Na, Ke):
	max = 0
	curr = 0
	stair = stairs(Na, Ke)
	for i in stair:
		if(i=='N'):
			curr+=1
			if(curr>max):
				max = curr
		else:
			curr-=1	
	return n-max

def war(n, Na, Ke):
	max = 0
	curr = 0
	stair = stairs(Na, Ke)
	for i in reversed(stair):
		if(i=='N'):
			curr+=1
			if(curr>max):
				max = curr
		else:
			curr-=1			
	return max

T = int(raw_input())
for t in range(T):
	n = int(raw_input())
	s = raw_input()
	Naomi = [float(elem) for elem in s.split()]	
	Naomi = sorted(Naomi)
	s = raw_input()
	Ken = [float(elem) for elem in s.split()]	
	Ken = sorted(Ken)		
	print "Case #" + str(t+1) + ":", deceit(n, Naomi, Ken), war(n, Naomi, Ken)	


		
