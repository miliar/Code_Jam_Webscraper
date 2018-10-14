## Cookie Clicker Alpha problem
## Solution program code


f=open("B-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([float(s) for s in line.split()])

N=int(input_lines2[0][0])

g = open("output.out", 'w')
for i in range(N):
    C=input_lines2[i+1][0]
    F=input_lines2[i+1][1]
    X=input_lines2[i+1][2]
    buy=int((((X-C)*F/C-2)//F)+1)
    time=0.0
    speed=2.0
    for j in range(buy):
        time+=C/speed
        speed+=F
    time+=X/speed
    g.write('Case #'+str(i+1)+': '+str(time)+'\n')

g.close()

