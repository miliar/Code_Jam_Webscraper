t=int(raw_input())
for k in range(t):
    inp= raw_input()
    inp=inp.split(" ")
    m=inp[0]
    n=int(inp[1].strip())
    count=0
    s=list(m)
    countm=len(s)+1
    i=0
    while i<len(s):
        if s[i]=='-':
            flag=0
            if (n+i)>=len(s)+1:
                break
            for j in range(n):
                count=count+1
                if s[j+i]=='-':
                    s[j+i]='+'
                elif s[j+i]=='+':
                    flag=1
                    s[j+i]='-'
                    countm=min(countm,j+i)
            if flag:
                i=countm
            else:
                i=i+n

        else:
            i=i+1
    flag=0
    i=len(s)-1
    while i>=0:
        if s[i]=='-':
            flag=1
            break
        i=i-1
    if flag==1:
        print "Case #"+str(k+1)+": IMPOSSIBLE"
    else:
        print "Case #"+str(k+1)+": "+str(count/n)
