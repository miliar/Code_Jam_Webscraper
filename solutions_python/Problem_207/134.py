def f(n,r,o,y,g,b,v):
    rl = []
    yl = []
    bl = []
    if o + b == n:
        if o == b:
            return 'OB' * o
    if g + r == n:
        if g == r:
            return 'GR' * g
    if y + v == n:
        if y == v:
            return 'YV' * y

    # print(r,y,b)
    if o:
        b -= (o + 1)
        s = 'B' + 'OB' * o
        bl.append(s)
    if g:
        r -= (g + 1)
        s = 'R' + 'GR' * g
        rl.append(s)
    if v:
        y -= (v + 1)
        s = 'Y' + 'VY' * v
        yl.append(s)
    if r < 0 or y < 0 or b < 0:
        return "IMPOSSIBLE"

    for i in range(r):
        rl.append('R')
    for i in range(y):
        yl.append('Y')
    for i in range(b):
        bl.append('B')
    return f2(rl,yl,bl)


def f2(rl,yl,bl):
    ans = []
    try:
        while True:
            r = len(rl)
            b = len(bl)
            y = len(yl)
            if r + b + y <= 3:
                break
            if r >= y and  r >= b:
                if y >= b:
                    s = rl.pop() + yl.pop() + rl.pop()
                    rl.append(s)
                else:
                    s = rl.pop() + bl.pop() + rl.pop()
                    rl.append(s)
            elif y >= b:
                if r >= b:
                    s = yl.pop() + rl.pop() + yl.pop()
                    yl.append(s)
                else:
                    s = yl.pop() + bl.pop() + yl.pop()
                    yl.append(s)
            else:
                if r > y:
                    s = bl.pop() + rl.pop() + bl.pop()
                    bl.append(s)
                else:
                    s = bl.pop() + yl.pop() + bl.pop()
                    bl.append(s)
        if r + b + y != 2 and r + b + y != 3:
            return "IMPOSSIBLE"
        if (max((r,b,y))) != 1:
            return "IMPOSSIBLE"
        ans = ""
        if rl:
            ans += rl[0]
        if bl:
            ans += bl[0]
        if yl:
            ans += yl[0]
        return ans
    except:
        return "IMPOSSIBLE"

def check(l,r,y,b):
    for i in range(len(l)):
        if l[i] == l[i-1]:
            return False
    if l[0] == l[-1]:
        return False
    d = {'R': 0, 'B': 0, 'Y': 0}
    for i in l:
        d[i] += 1
    if d['R'] != r:
        print('r mismatch')
        return False
    if d['B'] != b:
        print('b mismatch')
        return False
    if d['Y'] != y:
        print('y mismatch')
        return False
    return True





T = int(input())
for case in range(1, T+1):
    n,r,o,y,g,b,v = map(int, input().split())
    ans = f(n,r,o,y,g,b,v)
    # if ans != "IMPOSSIBLE" and check(ans,r,y,b) == False:
    #     print(ans)
    # if ans == "IMPOSSIBLE":
    #     if max(r,y,b) <= n //2:
    #         print("shoulda worked", r,y,b)
    print("Case #%s: %s" % (case, ans))

