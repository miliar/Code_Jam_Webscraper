import sys
inp=open("input.txt","r")
out=open("output.txt","w")
sys.stdin=inp
sys.stdout=out
T =int(raw_input())
for case in range(T):
    X, R, C= map(int,raw_input().split())
    if (R*C)%X != 0:
        ans = "RICHARD"
    elif X >= 7:
        ans = "RICHARD"
    elif X <= 2:
        ans = "GABRIEL"
    elif X >= 2*min(R, C):
        ans = "RICHARD"
    else:
        ans = "GABRIEL"
    print "Case #"+str(case+1)+ ": "+str(ans)
inp.close()
out.close()
