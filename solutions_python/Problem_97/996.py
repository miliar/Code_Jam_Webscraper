import itertools
f=open("C.in","r")
wf=open("out.txt","w+")
def rotate(l,n):
    return l[-n:] + l[:-n]
def rotations(aList):
    q=[]
    for i in range(len(aList)):
        q.append(rotate(aList,i))
    return q

for i in range(int(f.readline())):
    c=f.readline()
    s=c.split()
    A=int(s[0])
    B=int(s[1])
    g=0
    p=[]
    mapped=[]
    check=[]
    for d in range(A,B+1):
        if str(d) in p and str(d) not in mapped:
#get all recycled pairs
            allperms=rotations(str(d))
            mapped+=allperms
            numbersInRange=0
            for xx in allperms:
                if int(xx)>=A and int(xx)<=B:
                    for yy in allperms:
                        if int(yy)>=A and int(yy)<=B and int(yy)>int(xx):
                            numbersInRange+=1
                            if xx+":"+yy in check:
                                numbersInRange-=1
                            check.append(xx+":"+yy)
            g+=numbersInRange
        else:
            p+=rotations(str(d))
#    print "Case #"+str(i+1)+": "+str(g)
    wf.write("Case #"+str(i+1)+": "+str(g)+"\n")
f.close()
wf.close()
