#lawnmower
# standard functions
#File input
file2test="B-small-attempt0.in"
#clears outfile.txt
outfileFlush=open("outfile.txt", "w")
outfileFlush.write("")
outfileFlush.close()


def writeout(answer,x):
#converts query from main loop (which is the answer list - ie place in list of items that add up to credit)
        answerTXT=""
        #print answer
        ##raw_input("in writeout")
        #if answer=="":
        #    return
        #for q in answer:
        #answerTXT=answerTXT+answ" "+q #might neeed str(q)
        answerTXT="Case #"+str(x)+": "+str(answer)+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)


        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        outfile.close()#pass


def readlawn(size):#,cases):
	n=int(size[0])
	m=int(size[1])
	print "n.m",n,m
	lawn=[]
	for x in range(1,n+1):
		line=file2.readline().split()
		lawn.append(line)
	#make columns
	column=[]
	for y in range(m):
		col=""
		for row in lawn:
			col=col+row[y]
			
		column.append(col)
		
	print "l,c",lawn,column
	return (lawn,column)
		
def checklawnA(lawn):
	#look for "1"s
	flag=0
	for row in lawn[0]:#?
		print row,row[0]
		if "1" in row:
			if checkrows(row,lawn)=="No":return "NO"
			print "cr-rl",checkrows(row,lawn)
	return "YES"
def checkrows(row,lawn):#,column):
	#either row or coumin indexed at row msut be ones
	low=0
	n=0
	ind=[]
	for h in row:
		if h=="1":
			low=low+1
			ind.append(n)
		n=n+1
	print "low",low
	if low ==1: 
	#check column
		col=lawn[1][ind[0]]
		for dig in col:
			if dig<>"1":return "No"
	if low==len(row):
		#it's ok
		return "OK"
	print "ind ", ind
	# what ifits between 1 and len ?
	print lawn
	print "col,ind,lawn[1]",ind,lawn[1]
	#if its part of a row
	for digf in ind:
		col=lawn[1][digf]
		print "col12 ",col
		for dig in col:
			if dig<>"1":return "No"
	

#main program loop
x=1 #?right place
cases=1
file2=open(file2test,"r")
no_cases=file2.readline().split()#dependent on structure as defined - this is just to ignore the first line for the purpose of this exercise
no_cases=int(str(no_cases[0]))
print(no_cases," numb of Cases pre-main while")
# now need to collect the next case
cases=1
while cases<=no_cases:
    #ncase=file2.readline().split()
    #blankline=file2.readline().split()
    #answer="UNKNOWN"
    size=file2.readline().split()
    
    ttb=readlawn(size)#case may not be needed
    #fred=checkcase(ncase)
    ted=checklawnA(ttb)
    answer=format(ted)
    #answer=msquare
    writeout(answer,cases)
    print cases,"case"
    cases=cases+1
file2.close()
print("Finished")

