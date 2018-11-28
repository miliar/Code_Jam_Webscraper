t=int(input())
case=1
while t:
    l=input().split()
    s=list(l[0]);

    k=int(l[1])
    steps=0;
    for i in range(k,0,-1):
        for j in range(len(s)-i):
            temp=s[j:j+i]
            if(temp.count('-')==i and j+k<=len(s)):
                steps+=1
                for kk in range(k):
                    temp=s[j+kk]
                    if(temp=='-'):
                        temp='+';
                    else:
                        temp='-';
                    s[j+kk]=temp;
            #s[j:j+i]=temp;

    #print(s)
    if(s.count('+')==len(s)):
        print("Case #"+str(case)+": "+str(steps));
    else:
        print("Case #"+str(case)+": IMPOSSIBLE" );
    case+=1
    #print("Case #"+str(case)+": "+ );
    t-=1
