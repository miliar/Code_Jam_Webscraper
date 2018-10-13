import sys

def func(a, kStr, n):
    if "0" not in a:
        return 0
    mina = 100000
    for i in range(n - k+1):
        string = i*"0" + kStr + (n - k -i)*"0"
        new = int(string, 2)
        anew = int(a, 2)
        ans = anew ^ new
        ans = str(bin(ans))[2:]
        if(len(ans) < n):
            (n-len(ans))*"0" + ans
        mina = min(mina, 1 + func(ans, kStr, n))
    return mina

def earlier(a, k):
    a = a.replace("+","1")
    a = a.replace("-","0")
    r = int(a,2)
    kStr = k*"1"
    print func(a, kStr, len(a))
    #print bin(r^)


def newer(a, k, n):
    count = 0
    for i in range(n-k+1):
        if(a[i]=="-"):
            count+=1
            temp = a[i:i+k]
            temp = temp.replace("+","?")
            temp = temp.replace("-","+")
            temp = temp.replace("?","-")
            a = a[:i] + temp + a[i+k:]
    if("-" in a):
        return -1
    else:
        return count

t = int(raw_input())
ansArr = []
for case in range(t):
    a, k = raw_input().split()
    k = int(k)
    ans = newer(a, k, len(a))
    if ans == -1:
        ansArr.append("Case #" + str(case+1) + ": IMPOSSIBLE")
    else:
        ansArr.append("Case #" + str(case+1) + ": " + str(ans))

f = open("../../Desktop/out.dat", "w+")

for i in ansArr:
    f.write(i + "\n")