from collections import deque

filename="input"

f=open(filename,"r")
cases = int(f.readline())
x=0

while x < cases:
	x+=1
	sz=(f.readline()).split()
	R=int(sz[0]) # RC counter
	k=int(sz[1]) # ppl allowed in RC
	N=int(sz[2]) # number of groups

	count=0
	money=0
	sz2=(f.readline()).split()
	l=deque([ int(num) for num in sz2 ])

	while count < R:
		count+=1
		sum = 0
		templist=[]
		while True:
			if len(l) <= 0: break
			item = l.popleft()
			#print item
			if (sum + item) <= k: 
				sum += item
				#print sum
				templist.append(item)
				#print templist
			else: 
				l.appendleft(item)
				break
		l.extend(templist)
		#print l
		money += sum
		#print money
	print "Case #%d: %d" % (x, money)

