# Bathroom Stalls2
# CodeJam 2017
# Istvan Szabo


import time
start=time.clock()
#f=open("A-small-attempt0.in")
#f=open("A-test.in")
f=open("A-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')


line_counter=0
for i in range(T):
    print(i)
    D=int(input_lines2[line_counter+1][0])
    N=int(input_lines2[line_counter+1][1])
    latest=-1
    for j in range(N):
        Ki=int(input_lines2[line_counter+2+j][0])
        Si=int(input_lines2[line_counter+2+j][1])
        arrival=(D-Ki)/Si
        if arrival>=latest:
            latest=arrival
    line_counter+=N+1
    g.write('Case #'+str(i+1)+': '+str(D/latest)+'\n')
g.close()
print(time.clock()-start)