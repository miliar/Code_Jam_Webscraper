def ispalindrome(x):
    #accept str
    lengthx=len(x)
    opposite=lengthx-1
    index=0
    while (opposite>=index):
        if x[index]!=x[opposite]:
            return False
        index+=1
        opposite-=1
    return True

def testrange(minim,maxim):
    from math import sqrt
    #need to be ints
    lelist=[]
    count=0
    #lerange=range(int(sqrt(minim)),maxim+1)
    #print lerange
    #print lerange
    x=int(sqrt(minim))
    while x<=maxim:
        #print i
        lesq=x*x
        if lesq>maxim:
            #print maxim
            return lelist
        if ispalindrome(str(x)):
            if ispalindrome(str(lesq)) and lesq>=minim:
                #print "abotu to append"
                lelist.append(lesq)
                count+=1
        x+=1
    return lelist

def howmany(mini,maxi,lelist):
    count=0
    for number in lelist:
        if number>=mini and number<=maxi:
            count+=1
    return count

fairsquares=testrange(1,100000000000000)
infile=open("C-large-1.in","r")
lines=infile.readlines()
numcases=int(lines[0])
for i in range(numcases):
    currentline=lines[i+1].rstrip().split()
    #print "ON THIS LINE:"
    #print currentline
    maxim=long(currentline[1])
    minim=long(currentline[0])
    #print minim
    #print maxim
    outtxt="Case #"+str(i+1)+": "+str(howmany(minim,maxim,fairsquares))
    #print outtxt
    print outtxt
