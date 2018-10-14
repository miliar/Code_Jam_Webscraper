from sys import stderr

# MISC
read_int = lambda:int(raw_input().strip())
read_ints = lambda:[int(x) for x in raw_input().split()]
count_to = lambda n:xrange(1,n+1)

# GENERAL SOLVE LOOP
def solve_all(solve):
    num_cases = read_int()
    for i in count_to(num_cases):
         print "Case #{0}:".format(i),
         solve()

# SOLUTION
def solve_case():
    num_rects = read_int()
    rects = [tuple(read_ints()) for i in count_to(num_rects)]
    bacteria = set()
    eastmost = set()
    southmost = set()
    vulnerable = set()
    for x1, y1, x2, y2 in rects:
        bacteria.update(
            (x,y)
            for x in xrange(x1,x2+1)
            for y in xrange(y1,y2+1))
        eastmost.update(
            (x2,y)
            for y in xrange(y1,y2+1))
        southmost.update(
            (x,y2)
            for x in xrange(x1,x2+1))
        vulnerable.update(
            [(x1,y1)])
    for (x,y) in list(eastmost):
        if (x+1,y) in bacteria:
            eastmost.remove((x,y))
    for (x,y) in list(vulnerable):
        if (x-1,y) in bacteria or (x,y-1) in bacteria:
            vulnerable.remove((x,y))

    time_passed = 0
    while len(bacteria)>0:
        time_passed += 1
        dying = [
            (x,y)
            for (x,y) in vulnerable
            if ((x-1,y) not in bacteria and (x,y-1) not in bacteria)]
        born_east = [
            (x+1,y)
            for (x,y) in eastmost
            if ((x,y) in bacteria and (x+1,y-1) in bacteria)]
        for x,y in born_east:
            bacteria.add((x,y))
            eastmost.remove((x-1,y))
            eastmost.add((x,y))
        for x,y in dying:
            bacteria.remove((x,y))
            vulnerable.remove((x,y))
            eastmost.discard((x,y))
            if (x+1,y) in bacteria:
                vulnerable.add((x+1,y))
            if (x,y+1) in bacteria:
                vulnerable.add((x,y+1))
    print time_passed

solve_all(solve_case)
