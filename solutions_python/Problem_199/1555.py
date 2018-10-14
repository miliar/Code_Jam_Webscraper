# Revenge of the pancakes
# CodeJam 2017
# istvan

f=open("A-large.in")
#f=open("A-test.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')


for i in range(T):
    row=list()
    for s in input_lines2[i+1][0]:
        if s=='-':
            row.append(0)
        else:
            row.append(1)
    k=int(input_lines2[i+1][-1])
    count=0
    for j in range(len(row)-k+1):
        if row[j]==0:
            count+=1
            for m in range(k):
                row[j+m]=1-row[j+m]
    if sum(row)==len(row):
        g.write('Case #'+str(i+1)+': '+str(count)+'\n')
    else:
        g.write('Case #'+str(i+1)+': '+'IMPOSSIBLE'+'\n')
g.close()
