import re, sys

def solve(k, S):
    perm_list = permute_list(range(k))
    min_size = 500000
    for perm in perm_list:
        newS = ""
        for x in xrange(len(S)/k):
            for i in perm:
                newS += S[x*k+i]
        prevchar = newS[0]
        cur_size = 1
        for c in newS:
            if c != prevchar:
                cur_size += 1
                prevchar = c
        min_size = min(cur_size, min_size)
    return min_size

def permute_list(l):
    if len(l) == 1:
        return [l]
    ps = []
    for i in l:
        n = l[:]
        n.remove(i)
        for p in permute_list(n):
            ps.append([i]+p)
    return ps

def parse_input():
    if len (sys.argv) < 2:
        print "Enter an input filename please"
        return
    inp = open (sys.argv[1])

    lines = [re.sub(r'[\n\r]','',l) for l in inp.readlines()]
    num_cases = int(lines[0])
    line_num = 1
    for case in xrange(num_cases):
        k = int(lines[line_num])
        S = lines[line_num+1]
        line_num+=2

        soln = solve(k, S)
        print "Case #"+str(case+1)+":", soln

parse_input()