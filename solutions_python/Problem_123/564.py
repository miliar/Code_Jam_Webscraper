import sys
f = open(sys.argv[1])
cases = int(f.readline().strip())

for n in xrange(1,cases+1):
    ans = 0
    armin, no_motes = [ int(x) for x in f.readline().strip().split()]
    other_motes = [ int(x) for x in f.readline().strip().split() ]
    other_motes.sort() 
    #print armin
    #print other_motes
    for i in xrange(no_motes):
        m = other_motes[i]
        if m < armin: 
            armin += m
        else:
            add_sol = 0
            if armin - 1 != 0:
                add_armin = armin
                while add_armin <= m:
                    add_armin = 2 * add_armin - 1 
                    add_sol += 1

                if add_sol < no_motes - i:
                    armin = add_armin + m
                    ans += add_sol
                else:
                    ans += 1
            else: 
                ans += 1
                
    print 'Case #%d: %d'%(n, ans)
    #raw_input()
