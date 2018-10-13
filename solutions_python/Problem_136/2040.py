def solve(n):
    c,f,x = input().split()
    c = float(c)
    f = float(f)
    x = float(x)
    now = float(2.0)
    t = 0
    while ( ( x/now ) > ( x/(now+f)+c/now ) ):
        t += c/now
        now += f
    t += x/now
    print("case #%d: %.7f"%(n,t))

t = int(input())
for i in range(1,t+1):
    solve(i)
