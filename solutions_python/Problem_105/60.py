import sys
sys.setrecursionlimit(1200)

def explor(i):
    if i not in seen:
        seen.add(i)
        r = False
        for c in clas[i]:
            if not r:
                r = explor(c)
        return r
    return True

t, T = 0, int(input())
while t != T:
    t += 1

    clas = {}
    for i in range(int(input())):
        clas[i+1] = list(map(int, input().split()))[1:]

    for c in clas:
        seen = set()
        if explor(c):
            ans = 'Yes'
            break
        else:
            ans = 'No'
    
    print("Case #%d:" % t, ans)
