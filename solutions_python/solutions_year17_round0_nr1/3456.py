def flip(x):
    res=''
    for i in x:
        if i=="+":res+="-"
        else:res+="+"
    return res
def check(x):
    for i in x:
        if i!="-": return False
    return True
def solve(x,k):
    ans=0;ln=len(x)
    for i in xrange(ln-k+1):
        if x[i]=="-":
            x=x[0:i]+flip(x[i:i+k])+x[i+k:]
            ans+=1
    if "-" in x:
        return None
    return ans

for cc in xrange(int(raw_input())):
    x,y=map(str,raw_input().strip().split())
    y=int(y)
    res=solve(x,y)
    if res==None:
        print "Case #"+str(cc+1)+": IMPOSSIBLE"
    else:
        print "Case #"+str(cc+1)+": "+str(res)

        
