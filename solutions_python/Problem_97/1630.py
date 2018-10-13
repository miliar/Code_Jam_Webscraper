#f = open('D:\downloads(chrome)\C-small-attempt0.in', 'r')
with open('D:\\downloads(chrome)\\C-small-attempt0.in', 'r') as f:
    data = [map(int, line.split()) for line in f]

def shift(a,n):
    return a[n:]+a[:n]
    
#data=[3,[1,9],[10,40],[100,500]]
for i in range(1,data[0][0]+1):
    cnt=0
    A=data[i][0]
    B=data[i][1]
    for j in range(data[i][0],data[i][1]+1):
        n=j
        n=str(n)
        n=list(n)
        if(len(n)==1):
            continue
        if(len(n)==2):
            m=shift(n,1)
            m=int("".join(m))
            if(m<=B and m>j):
                cnt+=1
        if(len(n)==3):
            for l in range(1,3):
                m=shift(n,l)
                if(m[0]!='0'):
                    m=int("".join(m))
                    if(m<=B and m>j ):
                        cnt+=1
    thefile=open("outputc1.txt",'a')
    thefile.write("Case #" + str(i) + ": %s\n" % cnt)
    thefile.close()
