import sys
txt=open('A-small-attempt3.in')
A = [line.strip() for line in txt]
for i in range(len(A)):
    A[i]=list(A[i])
    for j in range(len(A[i])):
        if type(A[i][j]==str) and A[i][j]!=' ':
            A[i][j]=int(A[i][j])
def sum(i,M):
    if i>=3:
        return M[i-1]+sum(i-1,M)
    return 0
def answer(M):
    for j in xrange(2,len(M)):
        if sum(j,M)<j-2:
            M[2]+=1
            return 1+answer(M)
    return 0
for i in xrange(1,len(A)):
    print "Case #"+str(i)+": "+str(answer(A[i]))
