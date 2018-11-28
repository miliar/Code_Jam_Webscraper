def lastTidy(N):
    s=[x for x in str(N)]

    if len(s)==1:
        return s

    ans=[]
    for i in xrange(0,len(s)-1):
        if int(s[i])>int(s[i+1]):
            ans.append(str(int(s[i])-1))
            ans+=['9']*(len(s)-i-1)

            return ans

        ans.append(s[i])

    ans.append(s[-1])
    return ans

def tidy(N):
    a=lastTidy(N)
    ans=''
    for i in a:
        ans+=i
    return int(ans)

def rtidy(N):
    a=tidy(N)
    while a!=N:
        N=a
        a=tidy(N)

    return a

f=open("prob2large.txt","r")
T=int(f.readline())

ans=[]
for line in f:
    ans.append(rtidy(int(line)))

f.close()

b=open("ans2large.txt","w")
for i in xrange(len(ans)):
    b.write("Case #"+str(i+1)+": "+str(ans[i])+"\n")


b.close()
