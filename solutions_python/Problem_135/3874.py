import sys
f = open("out.txt","w+")
sys.stdout = f
t = int(raw_input())
i=1
while i<=t:
    r1 = int(raw_input())
    ls=[[]]*4
    ls1=[[]]*4
    for x in range(0,4):
        ls[x] = map(int,raw_input().split(" "))    
    r2 = int(raw_input())
    for x in range(0,4):
        ls1[x] = map(int,raw_input().split(" "))
    count=0
    ans=0
    for x in range(0,4):
        for y in range(0,4):
            if ls[r1-1][x]==ls1[r2-1][y]:
                ans=ls[r1-1][x]
                count+=1
    if count==0:
        print 'Case #'+str(i)+': Volunteer cheated!'
    elif count>1:
        print 'Case #'+str(i)+': Bad magician!'
    else:
        print 'Case #'+str(i)+': '+str(ans)
    i+=1    
