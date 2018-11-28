import sys
sys.stdout=open('out.txt','w')
sys.stdin=open('C-small-attempt1.in','r')
t=input()
for y in range(t):
    t=raw_input().split(' ')
    a,b=int(t[0]),int(t[1])
    count=0;
    for i in range(a,b+1):
        snum=str(i)
        l=len(snum)
        for k in range(1,len(snum)):
            t=snum[-k:]+snum[:l-k]
            if int(t)>i and int(t)<=b:
                count+=1
    case='Case #'+str(y+1)+': '
    print case+str(count)
          
