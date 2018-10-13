def cake(nameList):
	lineLength=len(nameList[0])
	lines=len(nameList)
	beenUsed=[]
	for lineIndex,line in enumerate(nameList):
		lastCell="popo"
		for cellIndex,cell in enumerate(line):
			if(cell!='?' and cell in beenUsed):
				continue
			else:
				if cell!='?' and cell not in beenUsed:
					beenUsed.append(cell)
				
				
			#print "#"*5
			#print "lineIndex "+str(lineIndex)
			#print "cellIndex "+str(cellIndex)
			st=cellIndex
			en=cellIndex
			
			
			x=cellIndex+1
			cont=True
			while x<lineLength and cont:
				if(line[x]=='?'):
					line[x]=cell
				else:
					#print "asdasdasd"
					if(line[x]==cell):
						en=x
					else:
						en=x-1
					cont=False
				x+=1
			if cont and x>=lineLength:
				#print "asperger"
				en=lineLength-1
			##############
			x=cellIndex-1
			cont=True
			while x>-1 and cont:
				if(line[x]=='?'):
					line[x]=cell
				else:
					if(line[x]==cell):
						st=x
					else:
						st=x+1
					cont=False
				x-=1
			if cont and x<0:
				st=0
			#############
			#print 'st '+str(st)
			#print 'en '+str(en)
			
			###
			#print "\n\n"
			#printCake(nameList)
			#print "\n\n"
			
			y=lineIndex+1
			cont=True
			while y<lines:
				for i in xrange(st,en+1):
					if(nameList[y])[i]!='?':
						cont=False
						break
				if cont==False:
					break
				for i in xrange(st,en+1):
					(nameList[y])[i]=cell
				y+=1
			#############
			y=lineIndex-1
			cont=True
			while y>-1:
				for i in xrange(st,en+1):
					if(nameList[y])[i]!='?':
						cont=False
						break
				if cont==False:
					break
				for i in xrange(st,en+1):
					(nameList[y])[i]=cell
				y-=1
			#print "\n\n"
			#printCake(nameList)
			#print "\n\n"


def printCake(cakeList):
	for line in cakeList:
		print line,'\n'


#cakeList=[['C','O','D','E'],['?','?','?','?'],['?','J','A','M']]
#cakeList=[['?','?','?','?'],['?','C','J','?'],['?','?','?','?']]
#cakeList=[['G','?','?',],['?','C','?'],['?','?','J']]
#cakeList=[['C','A'],['K','E']]
#printCake(cakeList)
#print "\n\n"
#cake(cakeList)
#print "\n\n"
#printCake(cakeList)

#n='''
f=open("C:\\Users\\Saar\\Desktop\\input.txt",'r')
f2=open("C:\\Users\\Saar\\Desktop\\output.txt",'w')
lines=f.readlines()[2:]
cakeList=[]
line=[]
counter=1
for line in lines:
	lineList=[]
	if not (any(char.isdigit() for char in line)):
		for ch in line:
			if ch=='?' or ch.isalpha():
				lineList.append(ch)
		cakeList.append(lineList)
		continue
		
	
	cake(cakeList)
	f2.write("Case #"+str(counter)+":\n")
	for y in cakeList:
		f2.write(''.join(y)+"\n")
	cakeList=[]
	counter+=1

#printCake(cakeList)
cake(cakeList)
#printCake(cakeList)
f2.write("Case #"+str(counter)+":\n")
for y in cakeList:
	f2.write(''.join(y)+"\n")

f.close()
f2.close()
#'''



#['G','?','?',]
#['?','C','?']
#['?','?','J']