import math
from itertools import combinations as comb

##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt2.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

##def solve(n, k, rs, hs):
##    print n, k
##    for i in range(n):
##        print rs[i], hs[i]
##    ps = [(rs[i], hs[i], 2 * rs[i] * hs[i] + rs[i] * rs[i]) for i in range(n)]
##    ps.sort(key = lambda tup: tup[2], reverse=True)
##    print ps
##    total = 0
##    for i in range(k):
##        total += ps[i][0] * ps[i][1] * 2
####    print total
##    total += max([ps[i][0] * ps[i][0] for i in range(k)])
####    print total
##    return total * math.pi

def solve(n, k, rs, hs):
##    print n, k
##    for i in range(n):
##        print rs[i], hs[i]
    ps = [(rs[i], hs[i], 2 * rs[i] * hs[i] + rs[i] * rs[i]) for i in range(n)]
    ps.sort(key = lambda tup: tup[2], reverse=True)
##    print ps
    count = 1
    bottom_radius = ps[0][0]
    total = ps[0][0] * ps[0][1] * 2
    while count < k:
        ps.pop(0)
        incremental_area = [0 if ps[i][0] <= bottom_radius else ps[i][0] * ps[i][0] - bottom_radius * bottom_radius for i in range(len(ps))]
        ps = [(ps[i][0], ps[i][1], ps[i][0] * ps[i][1] * 2 + incremental_area[i]) for i in range(len(ps))]
        ps.sort(key = lambda tup: tup[2], reverse=True)
##        print 'ps00', ps[0][0], 'ps01', ps[0][1]
        total += ps[0][0] * ps[0][1] * 2
        bottom_radius = max(bottom_radius, ps[0][0])
        count += 1
    total += bottom_radius * bottom_radius
    return total * math.pi


##def solve(n, k, rs, hs):
##    m = 0
##    for c in comb(range(n), k):
####        print c
##        total = 0
##        rh = []
##        for i in c:
##            rh.append((rs[i], hs[i]))
##        rh.sort(key = lambda tup: tup[0], reverse=True)
##        total += rh[0][0] * rh[0][0]
##        for i in range(k):
##            total += rh[i][0] * rh[i][1] * 2
##        m = max(total, m)
##    return m * math.pi
        

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        n, k = read_ints()
        rs = []
        hs = []
        for i in range(n):
            r, h = read_ints()
            rs.append(r)
            hs.append(h)
##        if case == 8:        
        solution = solve(n, k, rs, hs)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
