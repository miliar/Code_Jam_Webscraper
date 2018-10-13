import math
fin=open("ra.in","r")
fout=open("ra.out","w")
T=int(fin.readline().strip())
def work(V):# V is a list of N integers
    global need
    S=[(V[i]+0.0)/(need[i]+0.0) for i in range(N)]
    #print V
    S1=list(S)
    S1.sort()
    high=S1[0]/0.9
    low = S1[-1]/1.1
    test=int(high)
    for y in range(test-2,test+3):
#        print y
        work='yes'
        for i in range(N):
            if 9*y*need[i]>10*V[i] or 11*y*need[i]<10*V[i]:
                work='no'
            #    print i,9*y*need[i], 10*V[i], 11*y*need[i]
                break
        if work=='yes':
            return 1
    return 0
for dummy in range(T):
    count=0
    print dummy+1
    if dummy>0:
        fout.write('\n')
    fout.write('Case #'+str(dummy+1)+': ')
    [N,P] = [int(x) for x in fin.readline().split()]
    need=[int(x) for x in fin.readline().split()]# how many ingredients we need
    M=[]
    for j in range(N):
        M.append([int(x) for x in fin.readline().split()])# M[i] is the list of guys we have of type i
    for j in range(N):
        M[j].sort()
    start=[0 for j in range(N)]
    while max(start)<P:
        D=[M[i][start[i]] for i in range(N)]
        if work(D)==1:
            for i in range(N):
                start[i]+=1
            count+=1
        else:
            D=[(i,(M[i][start[i]]+0.0)/need[i]) for i in range(N)]
            D.sort(key=lambda x:x[1])
            j=D[0][0]
            start[j]+=1
    fout.write(str(count))
