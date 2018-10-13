r_fname="A-large.in"
w_fname="output_l.txt"
with open(r_fname,"r") as input,open(w_fname,"w+") as output:
    t=int(input.readline())
    for m in range(1,t+1):
        n,k=input.readline().split()
        k=int(k)
        li=list(n)
        l=len(li)
        x=0
        flag=0
        for i in range(l-k+1):
            if li[i]=='-':
                x=x+1
                c=0
                while c<k:
                    if li[i+c]=='-':
                        li[i+c]='+'
                    elif li[i+c]=='+':
                        li[i+c]='-'
                    c=c+1
        s1=''.join(li)
        for i in range(l):
            if li[i]=='-':
                output.write("Case #%d: IMPOSSIBLE\n"%(m))
                flag=1
                break
        if flag==0:
            output.write("Case #%d: %d\n"%(m,x))

