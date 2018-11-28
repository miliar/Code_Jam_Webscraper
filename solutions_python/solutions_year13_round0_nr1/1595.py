
def solved(line):
	s = set(line)
	if len(s)==1:
		if '.' in s:
			return None
		elif 'X' in s:
			return 'X'
		else:
			return 'O'
	if len(s)==2 and 'T' in s:
		if 'X' in s:
			return 'X'
		else:
			return 'O'
	return None
		

def solve(ll):
	def isvertical(ll,i):
		return solved(''.join([ll[x][i] for x in range(4)]))
	def ishorizontal(ll,i):
		return solved(ll[i])
	def isdiagA(ll):
		return solved(''.join([ll[x][x] for x in range(4)]))
	def isdiagB(ll):
		return solved(''.join([ll[3-x][x] for x in range(4)]))
		
	if isdiagA(ll) is not None:
		return isdiagA(ll)
	if isdiagB(ll) is not None:
		return isdiagB(ll)
	for i in range(4):
		if ishorizontal(ll,i) is not None:
			return ishorizontal(ll,i)
		if isvertical(ll,i) is not None:
			return isvertical(ll,i)
	
	return None


tcases = int(raw_input())

for i in xrange(tcases):
	ll = [raw_input() for _ in range(4)]
	s = solve(ll)
	if s is None:
		uncompleted = any(['.' in l for l in ll])
		if uncompleted:
			print "Case #%d: Game has not completed" % (i+1)
		else:
			print "Case #%d: Draw" % (i+1)
	else:
		print "Case #%d: %s won" % (i+1,s)
	if i<tcases-1:
		raw_input()

