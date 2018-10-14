def flip(s,i,n):
    for j in range(n):
        tmp=s[i+j]
        sign=""
        if tmp=="-":
            sign="+"
        else:
            sign="-"
        s=s[:i+j]+sign+s[i+j+1:]
    return s

def fun(s,n):
    l=len(s)
    i=0
    c=0
    while i<l:
        if s[i]=="-":
            if i>l-n:
                return -1
            c=c+1
            s=flip(s,i,n)
        i=i+1
    return c

f_input=open("inputA.txt","r+")
f_output=open("outputA.txt","w+")
tc=int(f_input.readline())
for case in range(tc):
    s,tmp=f_input.readline().split(" ")
    n=int(tmp)
    ans=""
    tmp2=fun(s,n)
    if tmp2==-1:
        ans="IMPOSSIBLE"
    else:
        ans=tmp2
    f_output.write("Case #"+str(case+1)+": "+str(ans)+"\n")
    print "Case #"+str(case+1)+": "+str(ans)
f_input.close()
f_output.close()
