## Magic Trick problem
## Solution program code

import numpy ## Fairly generally used package


f=open("A-small-attempt0.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([int(s) for s in line.split()])

N=input_lines2[0][0]

g = open("output.out", 'w')
for i in range(N):
    rown1=input_lines2[1+i*10][0]
    rown2=input_lines2[6+i*10][0]
    A1=numpy.array(input_lines2[2+i*10:6+i*10])
    A2=numpy.array(input_lines2[7+i*10:11+i*10])
    row1=input_lines2[1+i*10+rown1]
    row2=input_lines2[6+i*10+rown2]
    p=0
    for e1 in row1:
        for e2 in row2:
            if e1==e2:
                p+=1
                answer=str(e1)
    if p==0:
        answer='Volunteer cheated!'
    elif p>1:
        answer='Bad magician!'
    g.write('Case #'+str(i+1)+': '+answer+'\n')

g.close()

