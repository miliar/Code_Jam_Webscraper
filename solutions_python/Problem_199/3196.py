# python 3
def flip(l, i, n):
    return l[:i]+l[i:i+n].replace("+","x").replace("-","+").replace("x","-")+l[i+n:]

def bfs(line, n):
    seen = set(line)
    queue = [(line,0)]
    while len(queue) > 0:
        #print(queue)
        l  = queue.pop(0)
        seen.add(l[0])
        if "-" not in l[0]:
            return l
        for i in range(len(l[0]) - n + 1):
            nl = flip(l[0], i, n)
            if "-" not in nl:
                return (nl,l[1]+1)
            if nl not in seen:
                seen.add(nl)
                queue.append((nl,l[1]+1))
    return ("", "IMPOSSIBLE")

t = int(input())
for i in range(t):
    l,n = input().split(" ")
    n = int(n)
    res = bfs(l, n)
    print("Case #" + str(i+1) + ": " + str(res[1]))
