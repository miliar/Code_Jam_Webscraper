def checkNum(num):
    num=str(num)
    num=list(num)
    num.sort()
    return num

def removeDup(num2):
    for s in range(1,len(num2)-1):
        num2=list(num2)
        if num2[s]==num2[s+1]:
            num2[s]="0"
            num2[s+1]="0"
    return num2

ANS=[]
a=raw_input()
a=int(a)
for i in range(a):
    b=raw_input()
    b=int(b)
    while True:
        s=checkNum(b)
        s=''.join(s)
        if int(s)==int(b):
            ANS.append(int(s))
            break
        else:
            b=str(b)
            b=removeDup(b)
            b=''.join(b)
            b=int(b)
            b=b-1
            pass
    
for ii in range(len(ANS)):
    print "Case #{}: {} ".format(ii+1, str(ANS[ii]))
