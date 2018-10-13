import sys,math


problemset = sys.argv[1]
inf = file('C-'+problemset+'.in')
outf = file('C-'+problemset+'.out','w')

N = int(inf.readline()) # Number of test cases

def cA(r):
	return math.pi*r*r

def sqA(s):
	if s < 0: return 0
	else: return s*s

def segArea(fiR,left,bottom):
	if left*left+bottom*bottom>fiR*fiR:
		#print 'segArea(',fiR,left,bottom,') = ',0
		return 0
	cX = math.sqrt(fiR*fiR-bottom*bottom)
	cY = math.sqrt(fiR*fiR-left*left)
	radian_size = (math.pi*fiR*fiR)/(2*math.pi)
	radians = abs(math.asin(cY/fiR)-math.asin(bottom/fiR))
	answer = radians*radian_size-(left*(abs(cY-bottom)/2)+bottom*(abs(cX-left)/2))
	#print 'segArea(',fiR,left,bottom,') = ',answer
	return answer
			
for testcase in xrange(N):
	(f,R,t,r,g) = map(float,inf.readline().split(' '))
	iR = R-t
	fiR = iR-f
	#print 'fly',f,'radius',R,'border',t,'string',r,'block',g
	A = cA(R) # Total area
	S = cA((R-t)-f) # Survival area without strings
	
	# Find open blocks in the top right quarter of the screen
	openSpace = 0
	openBlocks = 0
	blockSize = sqA(g-(2*f))
	numBlocks = int(math.ceil((R-(t+r))/(g+2*r)))
	for x in xrange(numBlocks):
		if x*(2*r)+(x+1)*(g)+r < fiR: xFull = True
		else: xFull = False
		for y in xrange(numBlocks):
			if y*(2*r)+(y+1)*(g)+r < fiR: yFull = True
			else: yFull = False
			
			# yFull could be set, not xFull
			left = r+(g+2*r)*x+f
			bottom = r+(g+2*r)*y+f
			
			if (left-f+g)*(left-f+g)+(bottom-f+g)*(bottom-f+g) <= fiR*fiR:
				openSpace += blockSize
				continue
			#print 'Block from',left,bottom,
			
			#if xFull and yFull:
			#	openSpace += blockSize
			#	openBlocks += 1
			#	continue
			#else:
			#	scale = 1
			#print ''
			#scale = 1
			rem = segArea(fiR,left+g-(2*f),bottom)+segArea(fiR,left,bottom+g-(2*f))-segArea(fiR,left+g-(2*f),bottom+g-(2*f))
			okarea = segArea(fiR,left,bottom)-rem
			#if okarea > blockSize:
			#print okarea,'>',blockSize
			#print 'fiR',fiR,'left/bottom',left,bottom,'x/y',x,y
			openSpace += okarea
	openSpace *= 4
	
	# For each open block, the amount of space for the fly is sqA(g-(2*f))
	ANSWER = (A-openSpace)/A
	#print '%.6f' % (ANSWER,)
	#if ANSWER < 0: ANSWER = 0.0
	print >> outf, "Case #"+str(testcase+1)+": "+'%.6f'%(ANSWER)
