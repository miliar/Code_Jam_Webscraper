#InfiniteHouseOfPancakes

def mushrooms(case, d, p):
	mush_s = p.split(' ')
	mush = makeInt(mush_s)
		
	m1 = method_1(mush)
	m2 = method_2(mush)
	print "Case #" + str(case) + ": " + str(m1) + " " + str(m2)
	
def method_1(mush):
	result = 0
	for i in range(len(mush)-1):
		if mush[i] > mush[i+1]:
			result += mush[i] - mush[i+1]
	return result
	
def method_2(mush):
	result = 0
	diff = 0
	
	for i in range(len(mush)-1):
		r = mush[i]-mush[i+1]
		if r > diff: 
			diff = r
			#print "new diff", diff
			
	for i in range(len(mush)-1):
		result += min(mush[i], diff)
		#print "new result", result
			
	return result
		
def makeInt(c):
	d = []
	for i in c:
		d.append(int(i))
	return d

inp = raw_input()
T = int(inp)

for i in range(T):
	new_inp = raw_input()
	pans = raw_input()
	mushrooms(i+1, int(new_inp), pans)
			
#mushrooms('1', '4', '10 5 15 5')
#mushrooms('1', '2', '100 100')
#mushrooms('1', '8', '81 81 81 81 81 81 81 0')
#mushrooms('1', '6', '23 90 40 0 100 9')
