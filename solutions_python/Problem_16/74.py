inp_file=file("D-small.in")
out_file=file("D-small.out","w")

def perm(k):
    num=0
    for c2 in range(5**k):
        temp=[]
        t_num=num
        for c1 in range(k):
            temp.append(t_num%5)
            t_num=t_num/5
        for c1 in range(k):
            if temp.count(c1)!=1:
                break
        else:yield temp
        num+=1

def enc(s,p):
    ns=""
    for c1 in range(0,len(s),len(p)):
        ts=s[c1:c1+len(p)]
        for num in p:
            ns+=ts[num]
    g=1
    prev=ns[0]
    for c1 in ns[1:]:
        if c1!=prev:
            g+=1
            prev=c1
    return g

def solve(k,s):
    best=len(s)
    for p in perm(k):
        t=enc(s,p)
        if t<best:best=t
    return str(best)

num=int(inp_file.readline())
for case in range(num):
    k=int(inp_file.readline()[:-1])
    s=inp_file.readline()[:-1]
    out_file.write("Case #%s: "%(case+1)+solve(k,s)+"\n")
inp_file.close()
out_file.close()
