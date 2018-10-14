#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ammar
#
# Created:     12/04/2014
# Copyright:   (c) Ammar 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open("inp.txt") as f:
        buff=f.readlines()
    cases=int(buff[0])
    lis=[]
    fil=open("Out.txt","w")
    for i in range(1,cases+1,1):
        line=buff[i]
        r=line.split()
        c=float(r[0])
        f=float(r[1])
        x=float(r[2])

        time=[]
        cps=[]
        time.append(0)
        cps.append(2)
        last=float(x/2)
        for j in range(1,int(x),1):
            time.append(time[j-1]+c/cps[j-1])
            cps.append(cps[j-1]+f)
            t_time=time[j]+x/cps[j]
            if last < t_time:
                break
            else:
                last=t_time
##        print last
        msg="Case #"+str(i)+": "+str(last)
        fil.write(msg+"\n");

if __name__ == '__main__':
    main()
