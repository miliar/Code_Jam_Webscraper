import sys

def func(n):
    a = str(n)
    l = len(a)
    if(l==1):
        return n
    for i in range(1,len(a)):
        print -i, -i-1, l-i
        if(a[-i] < a[-i-1]):
            a = a[:-i] + "9"*(i)
            a = a[:-i-1] + str(int(a[-i-1]) - 1) + a[-i:]
    return int(a)

t = int(raw_input())
ansArr = []
for case in range(t):
    n = int(raw_input())
    ans = func(n)
    if ans == -1:
        ansArr.append("Case #" + str(case+1) + ": IMPOSSIBLE")
    else:
        ansArr.append("Case #" + str(case+1) + ": " + str(ans))

f = open("../../Desktop/out.dat", "w+")

for i in ansArr:
    f.write(i + "\n")