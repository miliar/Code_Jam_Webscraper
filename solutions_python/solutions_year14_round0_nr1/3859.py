import sys
f = open('out.txt','w+')
test = int(raw_input().strip())
for k in xrange(1,test+1):
    first = int(raw_input().strip())
    first = first-1
    ls=[[]]*4
    i=0
    while i<4:
        ls[i]=map(int,raw_input().strip().split(' '))
        i+=1
    second = int(raw_input().strip())
    second-=1
    ls2 = [[]]*4
    i=0
    while i<4:
        ls2[i]=map(int,raw_input().strip().split(' '))
        i+=1
    count=0
    flag=0
    a,b,c,d=ls[first][0],ls[first][1],ls[first][2],ls[first][3]
    #print a,b,c,d
    #print ls2[second]
    if a in ls2[second]:
        num=a
        count+=1
    if b in ls2[second]:
        if count==1:
            flag=1
        else:
            num=b
            count+=1
    if c in ls2[second]:
        if count==1:
            flag=1
        else:
            num=c
            count+=1
    if d in ls2[second]:
        if count==1:
            flag=1
        else:
            num=d
            count+=1
    if flag==1:
        print 'Case #'+`k`+': '+'Bad magician!'
    elif flag==0 and count==1:
        print 'Case #'+`k`+': '+`num`
    elif flag==0 and count==0:
        print 'Case #'+`k`+': '+'Volunteer cheated!'
