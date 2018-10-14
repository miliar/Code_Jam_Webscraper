t = int(input())
def dfs(r,y,b, prev):
    if r == y == b == 0:
        return ""
    if prev != "R" and r > 0:
        s = dfs(r-1,y,b,"R")
        if s is not None:
            return "R" + s
    if prev != "Y" and y > 0:
        s = dfs(r,y-1,b,"Y")
        if s is not None:
            return "Y" + s
    if prev != "B" and b > 0:
        s = dfs(r,y,b-1,"B")
        if s is not None:
            return "B" + s
    return None

for i in range(t):
    n, r, o, y, g, b, v = [int(x) for x in input().split(" ")]
    if (r>y+b) or (y>r+b) or (b>r+y):
        print("Case #" + str(i+1) + ": IMPOSSIBLE")
    else:
        a = [(r,"R"),(y,"Y"),(b,"B")]
        a = sorted(a)
        s = a[2][1] * a[2][0]
        s=""
        for j in range(a[2][0]):
            s += a[2][1]
            if j < a[1][0]:
                s += a[1][1]
            if a[2][0] - a[0][0] <= j:
                s += a[0][1]
        print("Case #" + str(i+1) + ": "+ s)

