
# Google Code Jam 2016 Round 1B Problem B. 


def solve(cs, js):
    
    if "?" not in (cs+js):
        return cs+" "+js

    c = [x for x in cs]
    j = [x for x in js]

    cl = []
    jl = []

    cl = solveBA(c)
    jl = solveBA(j)

    diff = 9999999
    mem = {}

    for x in cl:
        for y in jl :
            key = abs(int(x)-int(y))
            if key <= diff:
                diff = key
                if key in mem:
                    mem[key].append((x,y))
                else:
                    mem[key] = [(x,y)]

    l = mem[diff]
    l.sort(key=lambda x: x[0])
    
    cs = l[0][0]
    js = l[0][1]
    return str(cs)+" "+str(js)

def solveBA(l):
    res = []
    if len(l) == 0:
        return [""]

    if l[0] == "?":
        rlist = solveBA(l[1:])
        for i in range(10):
            for rs in rlist:
                res.append(str(i)+rs)
    else:
        rlist = solveBA(l[1:])
        for rs in rlist:
            res.append(str(l[0])+rs)

    return res

if __name__ == "__main__":
    global h, n, m
    t = int(input())
    for ti in range(t):
        c,j = input().split(" ")
        res = solve(c,j)
        print("Case #{0}: {1}".format(ti + 1, res))
