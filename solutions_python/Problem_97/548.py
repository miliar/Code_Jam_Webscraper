group = [{}]

def stuff(start,end):
    di = {}
    for i in range(start,end):
        num = str(i)
        small = [i]
        for k in range(len(num)-1):
            num = num[1:]+num[0]
            if num[0]=='0':
                continue
            tmp = int(num)
            if tmp<i and tmp not in small:
                small.append(tmp)
        if len(small)>1:
            small.sort()
            di[small[0]]=small
    group.append(di)
        


stuff(11,100)
stuff(101,1000)
stuff(1001,10000)
stuff(10001,100000)
stuff(100001,1000000)
stuff(1000001,2000001)

    
c = int(raw_input())
for i in range(1,c+1):
    a,b = map(int,raw_input().split())
    l = len(str(a))-1
    d = group[l]
    answer=0
    for num in d:
        lis=d[num]
        s=len(lis)
        mn=0
        mx=s-1
        while mn<s and lis[mn]<a:
            mn+=1
        while mx!=mn and lis[mx]>b:
            mx-=1
        answer+=((mx-mn)*(mx-mn+1))/2
    print "Case #"+str(i)+": "+str(answer)
