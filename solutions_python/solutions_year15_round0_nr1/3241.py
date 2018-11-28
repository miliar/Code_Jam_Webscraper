## Standing Ovation
## Solution file

import math

f=open("A-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')

for i in range(T):
    smax=int(input_lines2[i+1][0])
    s=[]
    for si in input_lines2[i+1][1]:
        s.append(int(si))
    needed=0
    standup=0
    for j in range(smax+1):
        if standup<j and s[j]>0:
            needed=needed+(j-standup)
            standup=j
        standup=standup+s[j]
    g.write('Case #'+str(i+1)+': '+str(needed)+'\n')

g.close()
