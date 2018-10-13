#fi=open("A-small-attempt3.in",'r')#Input File
fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File
T=int(fi.readline())
for case in range(1,T+1,1):
    N=int(fi.readline())
    A=[]
    B=[]
    for n in range(0,N,1):
        temp= map(int, fi.readline().split())
        A.append(temp[0])
        B.append(temp[1])
    count=0
    for i in range(0,N,1):
        for j in range(i+1,N,1):
            if ((A[j]<=A[i] and B[j]<=B[i]) or (A[j]>=A[i] and B[j]>=B[i])):
                count=count
            elif ((A[j]<=B[i] and A[j]<=A[i] and B[j]<=B[i] and B[j]<=A[i]) or (A[j]>=B[i] and A[j]>=A[i] and B[j]>=B[i] and B[j]>=A[i])):
                count=count
            else:
                count=count+1
    fo.write("Case #"+str(case)+": "+str(count)+"\n")
    #print count
