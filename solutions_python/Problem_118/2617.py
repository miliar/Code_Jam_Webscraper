import math
def isPalin(num):
    """
    num=str(num)
    length=len(num)-1
    for i in range(length/2):
        if(num[i]!=num[length-i]):
            return False
    """
    num=str(num)
    if(num==num[::-1]):
        return True
    return False
count=0
t=input()
for i in range(t):
    count=0
    w=raw_input()
    w=[int(a) for a in w.split()]
    a=w[0]
    b=w[1]
    for u in range(a,b+1):
        if(isPalin(u)):
            sqr=math.sqrt(u)
            #print sqr
            if((int(sqr)==sqr) and isPalin(int(sqr))):
                count+=1
    print 'Case #'+str(i+1)+': '+str(count)
