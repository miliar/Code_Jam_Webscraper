def solve(c, f):
    res = 0
    x = [0 for i in f]
    f.sort(reverse=True)
    for i in range(len(f)):
        if x[i] != 1:
            nofit = True
            otherstuff = False
            for j in range(i+1, len(f)):
                if x[j] != 1 and j != i:
                    otherstuff = True
                    if f[j] + f[i] <= c:
                        x[j] = 1
                        nofit = False
                        break
            res = res + 1
        x[i] = 1
    return str(res)  

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        numfiles, c= map(int, r.readline().split())
        f = map(int, r.readline().split())
        w.write('Case #{0}: {1}\n'.format(str(case), solve(c, f)))

