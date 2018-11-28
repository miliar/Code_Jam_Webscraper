#f = open("A-small-attempt0.in",'r')
f = open("A-large.in",'r')
#f = open("A-sample.in",'r')

output  = open("output.txt",'w')
cases =int(f.readline())
for case in range(1,cases+1):
    [R,C]=[int(j) for j in str.split(f.readline())]
    A=[f.readline().strip() for j in range(R)]
    harr = [sum([0 if c =='.' else 1 for c in row])for row in A]
    #print(harr)
    varr  = [sum([0 if A[y][x] =='.' else 1 for y in range(len(A))])for x in range(len(A[0]))]
    #print(varr)
    poss =True
    for j in range(R):
        for i in range(C):
            if (A[j][i] !='.') and harr[j]==1 and varr[i]==1:
                poss = False
    if not poss:
        output.write("Case #"+str(case)+": IMPOSSIBLE\n")
    else:
        wrongArr=0
        for j in range(R):
            i=0
            while (i<C) and A[j][i]=='.':
                i+=1
            if i<C and A[j][i]=='<':
                wrongArr+=1
            i=C-1
            while (i>-1) and A[j][i]=='.':
                i+=-1
            if i>-1 and A[j][i]=='>':
                wrongArr+=1
        for i in range(C):
            j=0
            while (j<R) and A[j][i]=='.':
                j+=1
            if j<R and A[j][i]=='^':
                wrongArr+=1
            j=R-1
            while (j>-1) and A[j][i]=='.':
                j+=-1
            if j>-1 and A[j][i]=='v':
                wrongArr+=1
        output.write("Case #"+str(case)+": "+str(wrongArr)+"\n")
    #print(A)
    #output.write("Case #"+str(case)+": "+str(ret)+"\n")
output.close()
f.close()
