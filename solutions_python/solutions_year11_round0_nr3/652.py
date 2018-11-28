import sys, itertools

def p_sum(xs):
    res = 0
    for x in xs:
        res ^= x #p_add(res, x)
    return res

import collections

def is_solution(used, values):
    if all(used): return False
    if all([not u for u in used]): return False
    a = [v for (i,v) in enumerate(values) if used[i]]
    b = [v for (i,v) in enumerate(values) if not used[i]]
    return p_sum(a) == p_sum(b)
    
def compute_extensions(cur, used, bits, values):
    return [i for (i,u) in enumerate(used) if not u and ((values[i] >> cur) & 1)]
    return [c for c in bits[cur] if not used[c]]

def calc_score(used, values):
    return sum([v for (i,v) in enumerate(values) if used[i]])

best_sol = []
best_sum = 0
    
def bb(values, cur_score, used, cur, bits):
    global best_sol, best_sum

    if cur >= len(bits):
        return
    
    if is_solution(used, values):
        cand = calc_score(used, values)
        if cand <= best_sum:
            best_sum = cand
            best_sol = list(used)
        else:
            #pass
            return
    
    ext = compute_extensions(cur, used, bits, values)
    
    if False:
        print "c: ", cur
        print "bits", bits
        print "u: ", used
        print "e: ", ext
        print "v: ", values
    
    if len(ext) == 0:
        bb(values, cur_score, used, cur + 1, bits)
    else:
        for e in ext:
            used[e] = True
            bb(values, cur_score + values[e], used, cur + 1, bits)
            used[e] = False

def bb2(values, cur_score, used, cur, bits):
    global best_sol, best_sum

    cand = calc_score(used, values)
    if cand > best_sum:
        return

    if is_solution(used, values):
        if cand <= best_sum:
            best_sum = cand
            best_sol = list(used)
        else:
            return

    def compute_extensions2(cur, used, bits, values):
        return [i for (i,u) in enumerate(used) if not u]
            
    ext = compute_extensions2(cur, used, bits, values)
    
    if False:
        print "c: ", cur
        print "bits", bits
        print "u: ", used
        print "e: ", ext
        print "v: ", values
    
    for e in ext:
        used[e] = True
        bb2(values, cur_score + values[e], used, cur + 1, bits)
        used[e] = False

def newer_method(values, n):
    global best_sum, best_sol
    best_sum = sum(values) + 1
    best_sol = []
    # 20 bits are required to hold all the values
    # group the values by which bits they affect
    bits = collections.defaultdict(list)
    for (i,v) in enumerate(values):
        for b in range(0,21):
            if (v >> b) & 1:
                bits[b].append(i)

    used = [False for a in values]
    bb2(values, 0, used, 0, bits)
    
    #print best_sol

    s = sum([v for (i,v) in enumerate(values) if not best_sol[i]])
    return s
    
def new_method(values, n):
    best_value = -1
    # a 1 bit means patrick gets it
    # values are sorted in ascending order
    i = 0
    e = 1 << n
    while i < e:
        i += 1
        s = []
        p = []
        for j in range(0, n):
            if (i >> j) & 1:
                p.append(values[j])
            else:
                s.append(values[j])
        if len(s) > 0 and len(p) > 0 and p_sum(s) == p_sum(p):
            return sum(s)
    assert("wtf!")
    
# silly solver for the N < 15 case
def brute_force(values, n):
    best_value = -1
    for i in range(1, 1 << n):
        s = []
        p = []
        for j in range(0, n):
            if (i >> j) & 1:
                s.append(values[j])
            else:
                p.append(values[j])
        if len(s) > 0 and len(p) > 0 and p_sum(s) == p_sum(p):
            #return max(sum(p), sum(s))
            #print i, s, p_sum(s), p, p_sum(p)
            best_value = max(best_value, sum(p), sum(s))
    return best_value

def main():
    filename = sys.argv[1]
    f = open(filename)
    o = open(filename + ".new.2.out", "wt")
    num_tests = int(f.readline())
    for t in range(1, num_tests+1):
        n = int(f.readline())
        values = [int(a) for a in f.readline().split()]
        # there exists a solution if there are an even number of each bit
        sol_exists = 0
        for v in values:
            sol_exists ^= v
        if sol_exists == 0: 
            values.sort()
            res = newer_method(values, n)
            #res = brute_force(values, n)
        else:
            res = -1
        print res
        o.write("Case #%d: " % t)
        if res >= 0:
            o.write("%d\n" % res)
        else:
            o.write("NO\n")
    o.close()
    
main()