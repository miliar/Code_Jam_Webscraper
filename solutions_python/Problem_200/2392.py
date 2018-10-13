from sys import argv
f = open(argv[1])
out = open(argv[2], "w")

t = int(f.readline().strip())

for case in range(t):
    n = map(int, f.readline().strip())
    l = len(n)
    for x in range(1, l):
        if n[-x] < n[-x-1]:
            for xx in range(-1, -x-1, -1):
                n[xx] = 9
            n[-x-1]-= 1

    res = "".join(map(str, n))
    out.write("Case #{}: {}\n".format(case+1, int(res)))
        
