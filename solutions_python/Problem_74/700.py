# google codejam problem A

# At first I did simulated the movements using simple robot logic,
# but then decided this recursive solution was better.

# goals[] is global	for this function
#  returns number of seconds required to complete all goals, starting at i,
#  given robot positions pos[] and free moves free[]

def seconds(i, pos, free):
	if i >= len(goals): return 0
	(goalbot, goalbutton) = goals[i]
	otherbot = 1-goalbot
	distance = abs(goalbutton - pos[goalbot])
	needed = 1+max(distance-free[goalbot],0)
	newpos = pos[:]; newpos[goalbot] = goalbutton
	newfree = free[:]; newfree[goalbot] = 0; newfree[otherbot] += needed
	return needed + seconds(i+1, newpos, newfree)
	
T = int(raw_input())

case = 1
while case <= T:
	line = raw_input()
	pieces = line.split()
	N = int(pieces[0])
	goals = [("OB".index(pieces[2*i+1]),int(pieces[2*i+2])) for i in range(N)]
	print "Case #%d: %d" % (case, seconds(0,[1,1],[0,0]))
	case += 1



