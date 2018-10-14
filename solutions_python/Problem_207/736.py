
def custom_compare(c1,c2):
    return c1['val']-c2['val']
def getColor(dic):
    if dic['color'] == 0:
        return 'R'
    elif dic['color'] == 1:
        return 'Y'
    else:
        return 'B'
def construct(c):
    ans = ""
    top = c[2]['val']
    nextTop = c[1]['val']
    least = c[0]['val']
    k = nextTop-least
    while k > 0:
        ans += getColor(c[2])
        ans += getColor(c[1])
        top -= 1
        nextTop -= 1
        k -= 1
    flag = 0
    while nextTop > 0 or least > 0:
        if top > 0:
            ans += getColor(c[2])
            top -= 1
        if flag == 1:
            ans += getColor(c[1])
            flag = 0
            nextTop -= 1
        else:
            ans += getColor(c[0])
            flag = 1
            least -= 1
    return ans


def fun(r,y,b):
    c = [{'color' : 0,'val' :r },{'color' : 1,'val' :y },{'color':2,'val' :b }]
    c.sort(cmp = custom_compare)
    c1 = c[0]['val']
    c2 = c[1]['val']
    c3 = c[2]['val']
    if c1 + c2 < c3:
        return "IMPOSSIBLE"
    else:
        return construct(c)
def solve():
    t = int(raw_input())
    i = 1
    while i <= t:
        n,r,o,y,g,b,v  = map(int,raw_input().split())
        x = fun(r,y,b)
        print "Case #" + str(i) + ": " + fun(r,y,b)
        i += 1
solve()
