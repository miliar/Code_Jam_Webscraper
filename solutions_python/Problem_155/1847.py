import math

inp = open("in.txt")
out = open("out.txt", "w+")

def write_case(index, result):
    out.write("Case #%d: %s\n" % (index+1, result))

cases = int(inp.readline())  

def solve_case():
    n, people = inp.readline().split()
    n = int(n) + 1
    
    add = 0
    up = 0
    for i in xrange(n):
        if up < i:
            more = i-up
            up += more
            add += more
        up += int(people[i])
        print "up %s" % up
    
    return add

for i in xrange(cases):
    print "case %s" % (i+1)
    write_case(i, solve_case())