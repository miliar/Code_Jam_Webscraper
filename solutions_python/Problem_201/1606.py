# Bathroom Stalls
# CodeJam 2017
# Istvan Szabo



f=open("C-small-2-attempt3.in")
#f=open("C-test.in")
#f=open("C-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')

for i in range(T):
    print(i)
    N=int(input_lines2[i+1][0])
    K=int(input_lines2[i+1][1])
    L={N:1}
    for j in range(K):
        maxL=max(L.keys())
        L[maxL]=L[maxL]-1
        if L[maxL]==0:
            del L[maxL]
        if maxL % 2 == 0:
            a1=maxL/2
            a2=maxL/2 - 1
        else:
            a1=(maxL-1)/2
            a2=(maxL-1)/2
        if a1 in L:
            L[a1]+=1
        else:
            L[a1]=1
        if a2 in L:
            L[a2]+=1
        else:
            L[a2]=1
    g.write('Case #'+str(i+1)+': '+str(round(a1))+' '+str(round(a2))+'\n')
g.close()
