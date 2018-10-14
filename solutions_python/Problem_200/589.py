import sys
name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    x=input()
    if len(x)==1:
        print("Case #%s: %s"%(testCase, x))
    else:
        index=-1
        for j in range(len(x)-1):
            if x[j]>x[j+1]:
                index=j
                break
        if index==-1:
            print("Case #%s: %s"%(testCase, x))
        else:
            ans=0
            index2=-1
            for i in range(index, 0, -1):
                if x[i]>x[i-1]:
                    index2=i
                    break
            if index2==-1 and x[0]=='1':
                print("Case #%s: %s" % (testCase, '9'*(len(x)-1)))
            elif index2==-1 and x[0]!='1':
                s=int(x[0])-1
                s=str(s)
                print("Case #%s: %s" % (testCase, s+'9'*(len(x)-1)))
            else:
                for i in range(len(x)):
                    if i<index2:
                        ans+=int(x[i])*(10**(len(x)-1-i))
                    elif i==index2:
                        ans+=(int(x[i])-1)*(10**(len(x)-1-i))
                    else:
                        ans+=9*(10**(len(x)-1-i))
                print("Case #%s: %s" % (testCase, ans))