tc=int(raw_input())
num=tc
ans=[]
while tc:
    [n,m]=map(int,raw_input("").split(' '))
    count=0
    for i in range(n,m+1):
        hold=str(i)
        if (i**0.5)-int(i**0.5)==0 and hold==hold[::-1]:
            sqrt=i**0.5
            hold=str(int(sqrt))
            if hold==hold[::-1]:
                count+=1
    ans.append(count)
    tc-=1
for i in range(len(ans)):
    print "Case #"+str(i+1)+": "+str(ans[i])
			
