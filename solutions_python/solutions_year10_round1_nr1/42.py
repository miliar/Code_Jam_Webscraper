#2 lines per test, including variable number of args

def analyze(val):
	if val=='.':
		return 0
	elif val=='R':
	 	return 1
	else:
		return 2

f=open('C:/Users/Meir/python/codejam/input1.txt', 'r')
g=open('C:/Users/Meir/python/codejam/output1.txt', 'w')	

TestSize=0

aline=f.readline()
bline=aline.split(" ")


Testsize=int(bline[0])

R_wins=0
B_wins=0
ksize=0

def checkwin(idx1, idx2, aboard):
	global ksize
	bsize=len(aboard)
	ourval=aboard[idx1][idx2]
	#check up
	if(idx1>=ksize-1):
		awin=1
		length=1
		curidx=idx1-1
		while(awin and curidx>=0):
			curval=aboard[curidx][idx2]
			if(curval!=ourval):
				break
			if(curval==ourval):
				length+=1
				curidx-=1
			if(length==ksize):
				return 1
	#check up forward diagonal
	if(idx1>=ksize-1):
		awin=1
		length=1
		curidx1=idx1-1
		curidx2=idx2+1
		while(awin and curidx1>=0 and curidx2<bsize):
			curval=aboard[curidx1][curidx2]
			if(curval!=ourval):
				break
			if(curval==ourval):
				length+=1
				curidx1-=1
				curidx2+=1
			if(length==ksize):
				return 1
	#check down forward diagonal
	if(idx1<=bsize-ksize):
		awin=1
		length=1
		curidx1=idx1+1
		curidx2=idx2+1
		while(awin and curidx1<bsize and curidx2<bsize):
			curval=aboard[curidx1][curidx2]
			if(curval!=ourval):
				break
			if(curval==ourval):
				length+=1
				curidx1+=1
				curidx2+=1
			if(length==ksize):
				return 1
	#check right
	if(idx2<=bsize-ksize):
		awin=1
		length=1
		curidx=idx2+1
		while(awin and curidx>=0):
			curval=aboard[idx1][curidx]
			if(curval!=ourval):
				break
			if(curval==ourval):
				length+=1
				curidx+=1
			if(length==ksize):
				return 1
	return 0
	
def winners(aboard):
	global R_wins, B_wins
	win1=0
	win2=0
	for idx1 in range(len(aboard)-1,-1,-1):
		#print idx1
		if aboard[idx1][0]==0:
			break
		for idx2 in range(len(aboard[1])):
			theval=aboard[idx1][idx2]
			if (theval==0):
				break
			if(win1 and win2):
				B_wins=1
				R_wins=1
				return
			elif(not win1 and theval==1):
				win1=checkwin(idx1,idx2,aboard)
			elif(not win2 and theval==2):
				win2=checkwin(idx1,idx2,aboard)
	B_wins=win2
	R_wins=win1
	return
	
for test in range(Testsize):
	global B_wins, R_wins, ksize
	B_wins=0
	R_wins=0
	#args from first line
	aline=f.readline()
	bline=aline.split(" ")
	bsize=int(bline[0])
	ksize=int(bline[1])
	
	newboard=[]
	for idx1 in range(bsize):
		newboard.append([])
		for idx2 in range(bsize):
			newboard[idx1].append(0)
	
	#grab args from 2nd line
	for idx in range(bsize):
		aline=f.readline()
		args=[]
		for idx2 in range(bsize):
			args.append(analyze(aline[idx2]))
		args.reverse()
		currow=0
		for item in range(len(args)):
			if args[item]==0:
				continue
			else:
				newboard[idx][currow]=args[item]
				currow+=1
	#for row in newboard:
	#	print row
	winners(newboard)
		
		
	output="Neither"
	#OUTPUT
	if (B_wins and R_wins):
		output="Both"
	elif(B_wins):
		output="Blue"
	elif(R_wins):
		output="Red"
	g.write("Case #" + str(test+1)+": "+ str(output) +"\n")