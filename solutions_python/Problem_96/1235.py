def get_all_comb():
    all = {}
    for s in range(31):
        nsup = set()
        sup = set()
        for p in range(11):
            for a in range(max(0,p-2), min(10, p)+1):
                for b in range(max(0, p-2), min(10, p)+1):
                    if a + b + p == s:
                        if p-a>=2 or p-b>=2:
                            sup.add(p)
                        else:
                            nsup.add(p)
        all[s] = (list(sup), list(nsup))
    return all

def get_flag(s, p, all):
    assert p>=0
    assert s>=0
    flag = 0
    sup, nsup = all[s]
    if nsup and nsup[0] >= p:
        flag += 1
    if sup and sup[0] >= p:
        flag += 2
    return flag

def main(filename):
    all = get_all_comb()
#    for s in all:
#        print s, all[s]
    
    f = open(filename)
    lines = f.readlines()
    f.close()
    T = int(lines[0])
    for i in range(1, T+1):
        line = lines[i]
        
        tokens = [int(t) for t in line.split()]
        N = tokens[0]
        S = tokens[1]
        p = tokens[2]
        G = tokens[3:]
        assert len(G) == N
        
        flags = []
        for g in G:
            flag = get_flag(g, p, all)
            flags.append(flag)
        flags_bak = flags[:]
            
        #print S, p, G, flags_bak
        res = 0
        for j in range(S):
            if 2 in flags:   # first count surprising only
                flags.remove(2)
                res += 1
            else:  # then both
                if 3 in flags:
                    flags.remove(3)
                    res += 1
        
        for f in flags:  # last only count both
            if f == 3 or f==1:
                res += 1
        
        print "Case #%d: %s" % (i, res)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])