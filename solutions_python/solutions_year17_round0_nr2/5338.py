import sys
def tidy(p):
    p=str(p)
    for j in range(0,len(p)-1):
        if int(p[j])<=int(p[j+1]):
            q=0
        else:
            q=1
            break
    return q
        

n=int(raw_input().strip())
val=[]
for i in range(n):
    k=int(raw_input())
    val.append(k)
c=1
for i in val:
    print "Case #",;sys.stdout.softspace=False;print c,;sys.stdout.softspace=False;print ":",
    c+=1
    if i<=9 and i>=1:
        print i
    else:
        z=0
        while(z>=0):
            x=tidy(i)
            if x==0:
                print i
                break
            elif x==1:
                i-=1
