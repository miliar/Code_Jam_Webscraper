t = int(raw_input())
ansArr = []

def func(d, n, horses):
    time = max(horses)
    return d/time

for case in range(t):
    d,n = map(int,raw_input().split())
    d = float(d)
    horses = []
    for i in range(n):
        a,b = map(float,raw_input().split())
        horses.append((d-a)/b)
    ans = func(d, n, horses)
    ansArr.append("Case #" + str(case+1) + ": " +  "%0.6f" % ans)

f = open("../../Desktop/out.dat", "w+")

for i in ansArr:
    f.write(i + "\n")