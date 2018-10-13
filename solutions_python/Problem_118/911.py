# standard functions
#File input
file2test="C-large-1.in"
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

def fairsql(cases):
	cases=int(cases)
	sqlimits=[]
	max1=0
	n=0
	while n<cases:
		fsql=file2.readline().split()
		fs,ql=int(fsql[0]),int(fsql[1])
		sqlimits.append([fs,ql])
		if max1<ql:max1=ql
		n=n+1
		print fsql
	print sqlimits #, fsql
	return (sqlimits,max1)

def lookforpalsq(fsql):
	#print fsql
	lower=int(fsql[0])
	upper=int(fsql[1])
#	lowersqr=int(lower**0.5)-1#might miss here
	found=0
	#need to chop 
	
	testsqs=[sq for sq in listsqs if sq>=lower and sq<=upper]
	print "testsqs ",testsqs
	#for sq in testsqs :
	#	if sq*sq in testsqs:found=found+1
	#	print "found ",found
#	if sq>upper:break
	#	print "SQs = ",sq,
	found=len(testsqs)
	return found
		#if checkpal(sq):
		#	checkpal(sq*sq)
		
		
		
		
		
def checkpal(numb):
	numb1=str(numb)
	numb2=""
	n=1
	lgth=len(numb1)
	for dig in numb1:
		numb2=numb2+numb1[lgth-n]
		n=n+1
#	print "numbs",numb1,numb2
	if int(numb1)==int(numb2):return True
	return False
	#find sqrt of lower as start point

def popsqs(maxl):#try poulating squares to check  - only does this once
	#lower=int(fsql[0])
	#upper=int(fsql[1])
	#sqlow=int(lower**0.5)-1
	#print upper,lower,sqlow
	#max1=int(max1**0.5)-1
	sq=1
	sqs=[]
	#n=sqlow
	n=1
	while sq<max1:
		sq=n*n
		if checkpal(sq):
			if checkpal(n):
				sqs.append(sq)#big integer problem?
		n=n+1
	print sqs	
	return sqs

#main program loop
x=1 #?right place
#cases=1
file2=open(file2test,"r")
no_cases=file2.readline().split()#dependent on structure as defined - this is just to ignore the first line for the purpose of this exercise
no_cases=int(str(no_cases[0]))
print(no_cases," numb of Cases pre-main while")
# now need to collect the next case
cases=0
(fsql,max1)=fairsql(no_cases)#case may not be needed
listsqs=popsqs(max1)

while cases<no_cases:
    #ncase=file2.readline().split()
    #blankline=file2.readline().split()
    #answer="UNKNOWN"
    #fred=checkcase(ncase)
    ted=lookforpalsq(fsql[cases])
    answer=format(ted)
    #answer=msquare
    cases=cases+1
    writeout(answer,cases)
    print cases,"case"
    #cases=cases+1
file2.close()
print("Finished")

