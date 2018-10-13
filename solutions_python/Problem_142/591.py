import sys
myin=open("b.in")
myout=open("aout1.txt",'a')
sys.stdin=myin
sys.stdout=myout
t=int(sys.stdin.readline())
for j in xrange(t):
    n=int(sys.stdin.readline())
    st1=str(sys.stdin.readline())
    st2=str(sys.stdin.readline())
    
    l1=[]
    l1_c=[]
    l2=[]
    l2_c=[]
    for i in st1:
        if i!='\n':
            if len(l1)==0:
                l1.append(i)
                l1_c.append(1)
            else:
                if l1[-1]==i:
                    l1_c[-1]+=1
                else:
                    l1.append(i)
                    l1_c.append(1)
    for i in st2:
        if i!='\n':
            if len(l2)==0:
                l2.append(i)
                l2_c.append(1)
            else:
                if l2[-1]==i:
                    l2_c[-1]+=1
                else:
                    l2.append(i)
                    l2_c.append(1)
    #print l1,l2
                    
    if len(l1)==len(l2):
        if l1==l2:
            moves=0
            for i in xrange(len(l1_c)):
                #print i
                moves+=abs(l1_c[i]-l2_c[i])
            print "Case #"+ str(j+1) + ": "+str(moves)
        else:
            print "Case #"+str(j+1) + ": Fegla Won"
    else:
        print "Case #"+ str(j+1) + ": Fegla Won"
myin.close()
myout.close()
