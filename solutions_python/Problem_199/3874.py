__author__ = 'Smaran'
count=0
def flip(x):
    b=""
    for a in x:
        if a=='+':
            b+='-'
        else:
            b+='+'
    return b

# sss="---"


def flipper(a):
    count=0
    s=int(a[1])
    p=a[0]
    l=len(p)
    nc=0
    pc=0
    sss=""
    curr=p[0:s]
    out=""

    for i in range(l):
        sss+="+"
    print(sss)
    for i in range(l-s):
        print(i,p[i])
        # if(nc+pc==s):
        #     flip(p[x-s+1:i])
        #     pass
        print("1. curr=",curr)
        if(curr[0]=='-'):
            print("flipping",curr)
            curr = flip(curr)
            count+=1

        out+=curr[0]
        curr=curr[1:]+p[i+s]
        print("2. curr=",curr)
        # elif(x=='+'):
        #     if(i+s>=l):
        #         o="impossibe"
        #         print(o)
        #         return o
        #     pc+=1

    if(curr[0]=='-'):
        print("flipping",curr)
        curr = flip(curr)
        count+=1
    out+=curr

    print("out=",out,count,"sss=",sss,"\n\n")

    if (out==sss):
        print("success")
        return str(count)
    else:
        return "IMPOSSIBLE"

    # oval="Case #"+str(k)+": "+str(actors)
    # print(oval)
    # return oval
#     outfile.write(oval)
#     outfile.write("\n")

file=("A-large.in")
# file=("inputs")
out=("outputs2.txt")
f=open(file,'r')
testcases=f.readline().strip('\n')
print(testcases)
outfile=open(out,'w')


for k in range(1,int(testcases)+1):
    print(k,": ",end='')
    a=f.readline().strip('\n').split()
    x=flipper(a)
    oval="Case #"+str(k)+": "+x
    print(oval)
    outfile.write(oval)
    outfile.write("\n")

