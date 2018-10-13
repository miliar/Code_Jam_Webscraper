out=open("out.txt","w")
T=int(input())
for case in xrange(T):
    Ac,Aj=map(int,raw_input().split())
    A1=[]
    A2=[]
    for i in xrange(Ac):
        A1.append(map(int,raw_input().split()))
    for i in xrange(Aj):
        A2.append(map(int,raw_input().split()))
    if max(Ac,Aj)==1:
        ans=2
    else:
        if Ac==2:
            A1=sorted(A1)
            if abs(A1[0][0]-A1[1][1])<=720 or A1[0][1]+1440-A1[1][0]<=720:
                ans=2
            else:
                ans=4
        if Aj==2:
            A2=sorted(A2)
            if abs(A2[0][0]-A2[1][1])<=720 or A2[0][1]+1440-A2[1][0]<=720:
                ans=2
            else:
                ans=4
            
    print ans
    out.write("Case #"+str(case+1)+": "+str(ans)+"\n")

out.close()                