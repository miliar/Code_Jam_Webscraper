from sys import stdin
def main():
    cont=1
    x=int(stdin.readline())
    for i in range(x):
        x1=stdin.readline()
        if len(x1)==1:
            print("Case #"+str(cont)+":",x1)
            cont+=1
        else:
            a=1
            b=list(x1)
            c=b[0:-1]
            f=[]
            for j in range(len(c)):
                f.append(int(c[j]))
            for j in range(1,len(f)):
                if f[-j]<f[-j-1]:
                    if f[-j]==0:
                        f[-j-1]-=1
                        f[-j]=9
                        for h in range(len(f)-j,len(f)):
                            f[h]=9
                    else:
                        f[-j-1]-=1
                        f[-j]=9
                        f[-j]=9
                        for h in range(len(f)-j,len(f)):
                            f[h]=9
                if f[-j]==0 and f[-j-1]==0:
                    f[-j]=9                
            d=""
            for j in range(len(f)):
                d+=str(f[j])           
            print("Case #"+str(cont)+":",int(d))
            cont+=1
main()
