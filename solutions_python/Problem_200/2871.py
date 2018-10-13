def decr(s,i):
    if i<0:
        return s
    tmp=int(s[i])
    if tmp==0:
        s=s[:i]+"9"+s[i+1:]
        return decr(s,i-1)
    else:
        s=s[:i]+str(tmp-1)+s[i+1:]
        return s
    
def find(s,l):
    i=1
    while i<l:
        if s[i-1]>s[i]:
            s=s[:i]+"9"*(l-i)
            s=decr(s,i-1)
            if i>1:
                i=i-1
        else:
            i=i+1
    return s

f_input=open("inputB1.txt","r+")
f_output=open("outputB1.txt","w+")
tc=int(f_input.readline())
for case in range(tc):
    s=f_input.readline().strip()
    l=len(s)
    tmp=find(s,l)
    i=0
    while i<l and tmp[i]=="0":
        i=i+1
    ans=tmp[i:]
    f_output.write("Case #"+str(case+1)+": "+ans+"\n")
    print ("Case #"+str(case+1)+": "+ans)
f_input.close()
f_output.close()
