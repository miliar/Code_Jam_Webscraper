#python
#ominoes
#from decimal import *
infile="D-small-attempt2.in" #prima.in"#"B-large-practice.in"
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
        answerTXT="Case #"+str(x+1)+": "+str(answer)+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)


        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        outfile.close()#pass

def writeout2(answer,field,x):
#converts query from main loop (which is the answer list - ie place in list of items that add up to credit)
        answerTXT=""
        #print answer
        ##raw_input("in writeout")
        #if answer=="":
        #    return
        #for q in answer:
        #answerTXT=answerTXT+answ" "+q #might neeed str(q)
        answerTXT="Case #"+str(x+1)+": "+""+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)
        

        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        for row in field:
          outfile.write(row+"\n")
        outfile.close()
        #pass


#cookie farm

#read in data
def readinp(infile):
    blocksz={}#testshy={}
    rowcol={}#testaud={}
    tests=0
    with open(infile,'r') as inputf:
        count=0
        for line in inputf:
            if count==0:
                value=line.split()
                tests=int(value[0])
                count=1
                continue
        
            value=line.split()
            #print value
            #print count
            #print tests
            blocksz[count]=int(value[0])#line.strip()
            rowcol[count]=(int(value[1]),int(value[2]))
            count=count+1
          # print(count,value,testcases[0])
    return(blocksz,rowcol,tests)
#testcases=[]#copy from site
#for line in
#testcases.append

#shyness 
#logic
# need at least 1 at aud[0], then 
#add up shyness players

def check(x,rc):# 4,1,4
    r=rc[0]
    c=rc[1]
    q=min(r,c)
    m=max(r,c)
    ric="RICHARD"
    gab="GABRIEL"
    print("r",r,"c",c,"x",x,r*c/x,(r*c)%x)
    if x==1:return(gab)
    if (r*c)%x<>0:
        print("MM")
        return('RICHARD')
    if q==1:
        print("A")
        if x>2 or (x==2 and m%2==1):
            return(ric)
        else: return(gab)    
    if q==2:
        print("b")
        if x==4:
            return(ric)
        elif x==3 and m<3:
            return(ric)
        elif x==2 or x==3:
            return(gab)
    if q==3:
        print("c")
        if x==4 and m<=3:
            return(ric)
        
        #if x==3 and
    if q==4:
        print("d")
        if m==1:
            print('Wring')
            return(ric)
    return(gab)
    return("bollo")
    

# ominoes - 1=1, 2=1, 3=2, 4=5
#1 - columns =1 Richard wins, if X>2, or X=2 AND r is odd
#2 - columns = 2 Richard wins if X=4 AND (r<=3), if X=3 AND r<3, [if X=2 Gabriel wins 
#3 - columns = 3 Richard wins if X=4 AND (r<=3), if X=3 AND r=1, if is odd
#4 - columns =4 Richard loses if X=4,unless r=1, wins if X=3, and r is even, losesifX=2, or 1
#if x=2, or x=4 and 
#if r*c/X is not an integer Richard wins



#start

#tstshy,tstaud,tests=readinp(infile)
blocksz,rowcol,tests=readinp(infile)
print blocksz,rowcol,tests
for a in range(tests):
    answer=check(blocksz[a+1],rowcol[a+1])
#    answer=needed(tstaud[a+1])
    writeout(answer,a)
    
    pass
#cases
# omnoes - 1=1, 2=1, 3=2, 4=5
#1 - columns =1 Richard wins, if X>2, or X=2 AND r is odd
#2 - columns = 2 Richard wins if X=4 AND (r<=3), if X=3 AND r<3, [if X=2 Gabriel wins 
#3 - columns = 3 Richard wins if X=4 AND (r<=3), if X=3 AND r=1, if is odd
#4 - columns =4 Richard loses if X=4,unless r=1, wins if X=3, and r is even, losesifX=2, or 1
#if x=2, or x=4 and 
#if r*c/X is not an integer Richard wins
 
