from copy import copy

sourcepath = '/Users/alistairpalfreyman/Documents/Code Jam/Input/D-large.in.txt'
destpath = '/Users/alistairpalfreyman/Documents/Code Jam/Output/D-large.out.txt'

def solve(naomi,ken):

	nd = copy(naomi)
	nw = copy(naomi)
	kd = copy(ken)
	kw = copy(ken)
	return str(solvedeceiptful(nd,kd)) + ' ' + str(solvewar(nw,kw))
	
	
def solvewar(naomi, ken):
	wins = 0
	for block in naomi:
		bigger = [b for b in ken if b > block]
		
		k2p = min(ken) if len(bigger)==0 else min(bigger)
		ken.remove(k2p)
		
		if block > k2p:
			wins +=1
			
	return wins
		
def solvedeceiptful(naomi, ken):
	delta = 0.00000001
	wins = 0
	
	# get rid of all the games naomi can't win...
	naomi.sort()
	ken.sort()
	
	# count games ken has to win
	while (len(naomi) > 0) and ((max(naomi) < max(ken)) or (min(naomi) < min(ken))):
		actual = min(naomi)
		k2p = max(ken)
		stated = max(ken)-delta
		
		ken.remove(k2p)
		naomi.remove(actual)

			
	while len(naomi) > 0:
		stated = max(ken) + delta
		k2p = min(ken)
		winners = [x for x in naomi if x > k2p]
		
		if len(winners) == 0:
			return wins + solvedeceiptful(naomi, ken)
		
		actual = min(winners)
		
		ken.remove(k2p)
		naomi.remove(actual)		
	
		if actual > k2p:
			wins += 1
		
	return wins	



fd = open(sourcepath, 'r')
fo = open(destpath, 'w')
T = int(fd.readline())
for i in range(1,T+1):
	N = int(fd.readline())
	naomi = [float(a) for a in fd.readline().split(' ')] 
	ken = [float(a) for a in fd.readline().split(' ')] 
	result = solve(naomi,ken)
	print 'Case #' + str(i) + ': ' + result + '\n',
	fo.write('Case #' + str(i) + ': ' + result + '\n')
	
fd.close()
fo.close()


	