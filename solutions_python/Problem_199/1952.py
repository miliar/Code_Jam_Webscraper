import sys
# C:\Users\Harshit\PycharmProjects\Test36\A-small.out
name = "A-large"
path = ""
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    x,n=input().split()
    n=int(n)
    x=list(x)
    res=0
    for i in range(len(x)-n+1):
        if(x[i]=="-"):
            for j in range(i,n+i):
                if(x[j]=="-"):
                    x[j]="+"
                else:
                    x[j]="-"
            res+=1
    x=set(x)
    l=len(x)
    if(l==1 and x=={"+"}):
         print("Case #" + str(testCase) + ": " +str(res))
    else:
         print("Case #" + str(testCase) + ": " +"IMPOSSIBLE")