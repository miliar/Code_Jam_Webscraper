import math
def solve(c,f,x):
    fsum=0
    start=2.0
    if x<=c:
        return x/start
    else:
        ans=(f*x-start*c)/(c*f)
        ans=math.ceil(ans)
        for j in range(1,ans):
            fsum=fsum+c/(start+f*(j-1))
        fsum=fsum+x/(start+f*(ans-1))
        return fsum

file=open('B-small-attempt3.in','r')
line1=file.readline()
cases=int(line1)
for case in range(1,cases+1):
    line=file.readline()
    prob=line.split()
    c=float(prob[0])
    f=float(prob[1])
    x=float(prob[2])
    print("Case #"+str(case)+ ": " + str(solve(c,f,x)))



