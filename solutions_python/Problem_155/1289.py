f = open('output.txt', 'w')
T=int(raw_input())
a=[]
for i in range(T):
    Smax,S=raw_input().split()
    Smax=int(Smax)
    if S[-1]=='0':
        print "error"
    n,k=0,0
    for j in range(len(S)):
        if n>j:
            n+=int(S[j])
        else:
            k+=j-n
            n=j
            n+=int(S[j])
    a.append(k)
for i in range(T):
    f.write("Case #"+str(i+1)+": "+str(a[i])+"\n")
