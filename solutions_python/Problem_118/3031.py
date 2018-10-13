import math

def read_inp(path):
    rr = file(path).read().splitlines()[1:]
    rr = [[int(y) for y in x.split(" ")] for x in rr]
    return rr

def solve_one(start, end):
    count = 0
    for x in xrange(start,end+1):
        if check_poly(x) and check_poly(math.sqrt(x)):
            count += 1
    return count

def solve(inp):
    res = [solve_one(x[0], x[1]) for x in inp]
    return res
    
def write_output(sol, path):
    f = file(path, "w")
    for i in xrange(len(sol)):
        f.write("Case #%d: %d\r\n"%(i+1, sol[i]))
    f.close()
        

def check_poly(x):
    if int(x) != x:
        return 0
    x = int(x)
    return str(x) == str(x)[::-1]

