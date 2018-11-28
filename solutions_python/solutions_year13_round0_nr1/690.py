# standard functions
#File input
file2test="A-large.in"
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

def readboard(ncase):
	#they are all four by four boards
	ttboard=[]
	for n in range(4): # 4 or 3?
		row=file2.readline().split()
		ttboard.append(row)
	print ttboard#DEBUG
	file2.readline().split()#nlank line after board
	return ttboard
		
def lookforwin(ttb):
	#rows
	flag=0
	for row in ttb:
		if "XXXX" in row or "XXXT" in row or "XXTX" in row or "XTXX" in row or "TXXX" in row : return "X won"
		if "OOOO" in row or "OOOT" in row or"OOTO" in row or "OTOO" in row or "TOOO" in row :return "O won"
		if "." in row[0]:flag=1
	col=["","","",""]
	n=0
	m=0
	for n in range(4):
	
		for row in ttb:
			#print "row",row,"col",col[n]
		#for m in range(4)#len(row[0])
		#if row[0]==None:continue
			#print "n", n
			col[n]=col[n]+row[0][n]
		#print "row",row,"col",col[n]
		#n=n+1
	#print "columns",col #:DEBUG
		
	#columns
	for row in col:
		if "XXXX" in row or "XXXT" in row or "XXTX" in row or "XTXX" in row or "TXXX" in row : return "X won"
		if "OOOO" in row or "OOOT" in row or"OOTO" in row or "OTOO" in row or "TOOO" in row :return "O won"
		
	#two diagonals
	diag1=["",""]
	n=0
	for row in ttb:
		#if row[0]==None:continue
		diag1[0]=diag1[0]+row[0][n]
		diag1[1]=diag1[1]+row[0][3-n]#going backwaards
		n=n+1
	#print diag1 #:DEBUG
	for row in diag1:
		if "XXXX" in row or "XXXT" in row or "XXTX" in row or "XTXX" in row or "TXXX" in row : return "X won"
		if "OOOO" in row or "OOOT" in row or"OOTO" in row or "OTOO" in row or "TOOO" in row :return "O won"
	if flag==1:
		return "Game has not completed"
	return "Draw"


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
    ttb=readboard(cases)#case may not be needed
    #fred=checkcase(ncase)
    ted=lookforwin(ttb)
    answer=format(ted)
    #answer=msquare
    writeout(answer,cases)
    print cases,"case"
    cases=cases+1
file2.close()
print("Finished")

