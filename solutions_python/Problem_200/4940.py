import sys
def issorted(ss):
    li=list(ss)
    li=[int(x) for x in li]
    if li==sorted(li):
        return True
    else:
        return False
def tidy(n):
    if(n<0):
        return 0
    if(issorted(str(n))):
        return n
    return tidy(n-1)
def tidy_large(n,m):
    a=(m+n)/2
    if(len(str(n))<5):
        return tidy(n,0)
    if(issorted(str(n))):
        return n
    if(n<m):
        return 0
    c=tidy_large(n-1,a)
    b=tidy_large(a-1,m)
    return max(c,b)
if __name__=="__main__":
    file=open("out.txt","w")
    i=0
    with open("aks.txt") as f:
        for line in f:
            if(len(line)<6):
                file.write("Case #"+str(i+1)+": "+str(tidy(int(line)))+"\n")
            else:
                file.write("Case #"+str(i+1)+": "+str(tidy_large(int(line),int(line)/2))+"\n")
            i+=1
        f.close()
    file.close()
