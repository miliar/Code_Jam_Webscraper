
t=int(raw_input())
for i in range(t):
    s=raw_input().split()
    k=int(s[1])
    s=s[0]
    j=0
    while True:
        w=s.find("-")
        if w==-1:
            break
        if w+k>len(s):
            j="IMPOSSIBLE"
            break
        s=list(s)
        for ww in range(w, w+k):
            s[ww]={"-":"+", "+":"-"}[s[ww]]
        s="".join(s)
        j+=1
    s="Case #"+str(i+1)+": "+str(j)
    print s
