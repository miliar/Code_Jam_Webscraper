import math
file = open("B-large.in","r")
outfile=open("outl2.txt","w")
t_case=file.readline()
def settle(cost,extra,goal):
    perSec=2
    time1=0
    while True:
        if(goal/perSec>cost/perSec+goal/(perSec+extra)):
            time1+=cost/perSec
            perSec+=extra
        else:
            return time1+goal/perSec


for k in range(0,int(t_case)):
    case=file.readline().split()
    listo=settle(float(case[0]),float(case[1]),float(case[2]))
    out="Case #"+str(k+1)+": "+str(listo)
    outfile.write(out+"\n")
    print(out)
