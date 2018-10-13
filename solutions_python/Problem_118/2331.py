import math
def ispalindrome(num):
    s=str(num)
    rev=s[::-1]
    if s==rev:
        return True
    else:
        return False
def solve(a,b):
    count=0
    for i in range(a,b+1):
        if ispalindrome(i):
            sp=math.sqrt(i)
            spint=int(sp)
            if spint==sp:
                if ispalindrome(spint):
                    count=count+1
    return count
f=open("C-small-attempt1.in","r")
f1=open("b_output.txt","w")
r=f.readlines()
case=1
for test in r[1:]:
    t=test.split(" ")
    a=int(t[0])
    b=int(t[1])
    out="Case #"+str(case)+": "+str(solve(a,b))+"\n"
    f1.write(out)
    case=case+1
f1.close()
f.close()
