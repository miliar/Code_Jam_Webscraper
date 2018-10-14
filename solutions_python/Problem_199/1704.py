def flip(x,c,visited,k):
    x1=x
    x=list(x)
    fli=[]
    d={'+':'-','-':'+'}
    for i in range(len(x)):
        if x[i]=='-':
            for j in range(k):
                if -j+i>=0 and k-j+i<=len(x):
                    y=list(x1)
                    for h in range(k):
                        y[h-j+i]=d[x[h-j+i]]
                    ans = "".join(y)
                    if ans not in fli:
                        if ans not in visited:
                            fli.append([ans, c + 1])
                            visited.append(ans)


    return fli
def start(x,k):
    st=[[x,0]]
    visited=[]
    finala="".join(['+']*len(x))
    ch=True
    while ch:
        if len(st)>0:
            tmp=st.pop(0)
            if tmp[0]==finala:
                return tmp[1]

            visited.append(tmp[0])
            ann=flip(tmp[0],tmp[1],visited,k)
            for i in ann:
                if i[0]==finala:
                    return i[1]

                else:
                    for i in ann:
                        st.append(i)
        else:
            return "IMPOSSIBLE"


f=open("/Users/balusunaresh/Desktop/A-small-attempt0.in.txt",'r')
for i in range(int(f.readline())):
    x=f.readline().split(" ")
    print "Case#"+str(i)+":"+str(start(x[0],int(x[1])))