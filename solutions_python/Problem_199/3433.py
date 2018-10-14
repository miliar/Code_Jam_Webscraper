f = open('A-large.in', 'r')
f2 = open('A-large-output.out', 'w')
k=0
nn=int(f.readline())
for line in f:
    k=k+1
    if k>nn:
        break
    ss=line.split()[0]
    s=list(ss)
    
    n=int(line.split()[1])
    c=0
    for p in range(0,len(s)-n+1):
        if(s[p]=='-'):
            c+=1
            for q in range(0,n):
                if(s[p+q]=='-'):
                    s[p+q]='+'
                else :
                    s[p+q]='-'
    w=0
    for p in range(len(s)-n,len(s)):
        if(s[p]=='-'):
            w=1
            break
    if w==1:
        f2.write("Case #"+str(k)+": IMPOSSIBLE\n")
    else:
        f2.write("Case #"+str(k)+": "+str(c)+'\n')
f.close()
f2.close()
