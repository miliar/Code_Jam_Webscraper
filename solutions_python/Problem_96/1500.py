
inf = open("input")

inp = inf.read()

inf.close()

inp = filter(None, inp.split("\n")[1:])

case = 1

f = open("output", "w")

for line in inp:
    inp = line.split(" ")

    S = int(inp[1])
    p = int(inp[2])
    N = [int(i) for i in inp[3:]]

    res = 0

    for n in N:
        #f = 2 if S > 0 else 1
        if (n-p)/2 >= p-1:
            res+=1
        elif S > 0:
            if (n-p)/2 >= p-2 and n != 0:
                res+=1
                S-=1

    f.write("Case #%s: %s\n" % (case, res))
    case+=1

f.close()