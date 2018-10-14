def digits(n):
    if n == 0:
        return [0]
    ret = []
    while n:
        ret.insert(0, n%10)
        n /= 10
    return ret

recycled_cache = {}

def recycled(n):
    digs = digits(n)
    seen = set([tuple(digs)])
    digs = digs[1:] + [digs[0]]
    ret = []
    while tuple(digs) not in seen:
        seen.add(tuple(digs))
        x = reduce(lambda x,y:x*10 + y, digs, 0)
        if x > n:
            ret.append(x)
        digs = digs[1:] + [digs[0]]
    return ret

for i in range(2000000):
    if i % 100000 == 0:
        print i
    recycled_cache[i] = recycled(i)

def solve_line(a, b):
    sol = 0
    for i in range(a, b):
        sol += len([r for r in recycled_cache[i] if r <=   b])
    return sol

def solve(path):
    out_path = path.replace("in", "out")

    with open(path) as fin:
        with open(out_path, "w") as fout:
            num_cases = int(fin.readline())
            print "Found", num_cases, "cases"

            for n in range(num_cases):
                a, b = [int(x) for x in fin.readline().strip().split()]
                sol = solve_line(a,b)
                fout.write("Case #%i: %i\n" % (n+1, sol))
                print "Case #%i: %i" % (n+1, sol)