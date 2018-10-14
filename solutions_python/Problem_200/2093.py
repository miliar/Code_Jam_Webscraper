import sys
# C:\Users\Harshit\PycharmProjects\Test36\A-small.out
name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    s=input()
    x=int(s)
    flag=0
    s=list(s)
    i=1
    while(i<len(s)):
        if (flag == 1):
            s[i]="9"
        elif s[i-1]>s[i]:
            change=i-1
            if(i>1):
                k=i-1
                for j in range(i-2,-1,-1):
                    change = j
                    if(s[j]!=s[k]):
                        change=j+1
                        break
            s[change]=str(int(s[change])-1)
            flag=1
            s[i]="9"
            i = change
        i+=1
    print("Case #" + str(testCase) + ": " +str(int("".join(s))))