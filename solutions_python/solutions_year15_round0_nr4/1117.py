t=int(raw_input())
fp=open('a.txt','w')
for _ in xrange(1,t+1):
    x,r,c=map(int,raw_input().split())
    p=r*c
    if x==1:
        ans='GABRIEL'
    elif x==2:
        if p%2==0:
            ans='GABRIEL'
        else:
            ans='RICHARD'
    elif x==3:
         if (p>4 and p!=8 and p!=16):
             ans='GABRIEL'
         else:
             ans='RICHARD'
    elif x==4:
         if p==12 or p==16:
             ans='GABRIEL'
         else:
             ans='RICHARD'
    fp.write('Case #%d: %s\n' %(_,ans))
fp.close()
