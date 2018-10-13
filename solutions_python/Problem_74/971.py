

def pairwise(iterable):
	a=iter(iterable)
	return zip(a,a)

def readlines():
	lines=[]
	file=open("input_large.in",'r')

	while True:
		line=file.readline().rstrip()
		if not line:
			break
		lines.append(line)
		pass
	numlines=int(lines[0])
	lines.pop(0)
	qlist=[]
	for line in lines:
		blah=[]
		blah=line.split(' ')
		queue=[] #queue of color/button tuples
		numButtons=blah[0]
		blah.pop(0)
		queue.append(numButtons)
		for x,y in pairwise(blah):
			queue.append((x,int(y)))
		qlist.append(queue)
	return (numlines,qlist)	

def tupIndex(l,c):
	" Find first instance of character in tuple list "
	try:
		i=[y[0] for y in l].index(c)
		return l[i]
	except:
		return (-1,-1)
def getNext(l):
	if len(l)>0:
		return l[0][0]
	else:
		return -1
def shortestSeq(queue):
	""" 
	To find the shortest path:
		Set the starting point of both colors
		Find the next position of both colors
		If the color is not at that position, move to it
		If the color is at that position and
			is first in the queue, press button
		If in position and not first, wait until it is first
	"""
	oLoc=oNext=1
	bLoc=bNext=1
	numButtons=queue[0]
	queue.pop(0)
	o=tupIndex(queue,'O')
	#[o[0] for o in queue].index('O')
	b=tupIndex(queue,'B')
	oNext=o[1]
	bNext=b[1]


	count=1
	#print "Time | Orange           | Blue"
	#print "-----+------------------+-----------------"
	while len(queue) > 0:
		s1="  %d  | " % count
		s2=" Stay at button %d " % oLoc
		s3=" Stay at button %d " % bLoc
		nextPush=getNext(queue)
		if nextPush == -1:
			break
		if oNext != -1:
			if oLoc != oNext:
				temp=oNext-oLoc
				temp=temp/abs(temp)
				oLoc+=temp
				s2=" Move to button %d " % oLoc
			elif oLoc==oNext and nextPush=='O':
				oPush=True
				s2=" Push button %d    " % oLoc
				queue.pop(0)
				o=tupIndex(queue,'O')
				oNext=o[1]
			elif oLoc==oNext and nextPush != 'O':
				s2=" Stay at button %d " % oLoc
		if bNext != -1:
			if bLoc != bNext:
				temp=bNext-bLoc
				temp=temp/abs(temp)
				bLoc+=temp
				s3=" Move to button %d " % bLoc
			elif bLoc==bNext and nextPush=='B':
				bPush=True
				s3=" Push button %d    " % bLoc
				queue.pop(0)
				b=tupIndex(queue,'B')
				bNext=b[1]
			elif bLoc==bNext and nextPush != 'B':
				s3=" Stay at button %d " % bLoc

		s=s1+s2+"|"+s3
		#print s
		count+=1
	return count-1

numlines,qlist=readlines()
f=open("out_large.out",'w')
for i in range(0,numlines):
	seconds=shortestSeq(qlist[i])
	print >>f, "Case #%d: %d" % (i+1,seconds)

