import math
def chk(lower,higher):
    count=0
    for e in range(lower,higher+1):
        a1=int(math.sqrt(e))
        b1=str(e)
        b2=b1[::-1]
        b3=int(b2)
        c1=str(a1)
        c2=c1[::-1]
        c3=int(c2)

        if a1*a1==e :
            if b3==e and c3==a1:
                count=count+1
    return count



file=open("c:/users/rhv/Desktop/code_jam/fands.txt.in","r")
i=0
m=file.readline()
l=m.split()
while i<int(l[0]):
    k=file.readline()
    k1=k.split()
    out=chk(int(k1[0]),int(k1[1]))
    print "Case #" + str(i+1) +": "+str(out)
    i=i+1


    



















            






                


   







    

                


                
        
