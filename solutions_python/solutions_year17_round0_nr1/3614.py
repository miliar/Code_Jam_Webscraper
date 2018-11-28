c=0
def convert(st,k,ind):
    if (len(st)-ind)<k:
        return -1
    else:
        global c
        c=c+1
        for i in range(ind,ind+k):
            if st[i]=="+":
                st[i]="-"
            elif st[i]=="-":
                st[i]="+"
        return st
fd=open("A-large.txt")
fd1=open("ouput.txt","w")
z=fd.read()
z=z.rstrip()
z=z.split("\n")
t=z[0]
for i in range(1,int(t)+1):
    c=0
    a=z[i].split(" ")
    st=a[0]
    st=list(st)
    k=a[1]
    k=int(k)
    while True:
        try:
            ind=st.index("-")
            st=convert(st,k,ind)
            if st==-1:
                fd1.write("case #"+str(i)+":"+" IMPOSSIBLE")
                fd1.write("\n")
                break
        except Exception as e:
            if c==0:
               fd1.write("case #"+str(i)+":"+" 0")
               fd1.write("\n")
               break
            else:
                fd1.write("case #"+str(i)+": "+str(c))
                fd1.write("\n")
                break
fd1.close()
fd.close()
