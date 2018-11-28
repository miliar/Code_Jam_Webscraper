import sys

def solve(R,C,g):
    done = set('?')
    
    for c in xrange(C):
        for r in xrange(R):
            if g[(r,c)] in done:
                continue
            else:
                done |= set(g[(r,c)])
            
            rl = r - 1
            while rl >= 0:
                if g[(rl,c)] != '?':
                    break
                rl -= 1
            rl += 1
            
            rh = r + 1
            while rh <= R-1:
                if g[(rh,c)] != '?':
                    break
                rh += 1
            rh -= 1
            
            for rr in xrange(rl,rh+1):
                g[(rr,c)] = g[(r,c)]
                
            cc = c-1
            while cc >= 0:
                safe = True
                for rr in xrange(rl,rh+1):
                    if g[(rr,cc)] != '?':
                        safe = False
                        break
                if safe:
                    for rr in xrange(rl,rh+1):
                        g[(rr,cc)] = g[(r,c)]
                else:
                    break
                cc -= 1

            cc = c+1
            while cc < C:
                safe = True
                for rr in xrange(rl,rh+1):
                    if g[(rr,cc)] != '?':
                        safe = False
                        break
                if safe:
                    for rr in xrange(rl,rh+1):
                        g[(rr,cc)] = g[(r,c)]
                else:
                    break
                cc += 1

def solve2(R,C,g):
    done = set('?')
    
    for r in xrange(R):
        for c in xrange(C):
            if g[(r,c)] in done:
                continue
            else:
                done |= set(g[(r,c)])
            
            rl = r - 1
            while rl >= 0:
                if g[(rl,c)] != '?':
                    break
                rl -= 1
            rl += 1
            
            rh = r + 1
            while rh <= R-1:
                if g[(rh,c)] != '?':
                    break
                rh += 1
            rh -= 1
            
            for rr in xrange(rl,rh+1):
                g[(rr,c)] = g[(r,c)]
                
            cc = c-1
            while cc >= 0:
                safe = True
                for rr in xrange(rl,rh+1):
                    if g[(rr,cc)] != '?':
                        safe = False
                        break
                if safe:
                    for rr in xrange(rl,rh+1):
                        g[(rr,cc)] = g[(r,c)]
                else:
                    break
                cc -= 1

            cc = c+1
            while cc < C:
                safe = True
                for rr in xrange(rl,rh+1):
                    if g[(rr,cc)] != '?':
                        safe = False
                        break
                if safe:
                    for rr in xrange(rl,rh+1):
                        g[(rr,cc)] = g[(r,c)]
                else:
                    break
                cc += 1

def isSolved(g):
    return '?' not in g.itervalues()
                
def getPut():
    [R,C] = map(int,raw_input().split())
    g = {}
    g2 = {}
    for r in xrange(R):
        line = raw_input()
        #print line
        for c in xrange(C):
            g[(r,c)] = line[c]
            g2[(r,c)] = line[c]
    #print
    solve(R,C,g)
    solve2(R,C,g2)

    if isSolved(g):
        gg = g
    elif isSolved(g2):
        gg = g2
    else:
        print "3456"
        gg = g
            
    for r in xrange(R):
        for c in xrange(C):
            sys.stdout.write(g[(r,c)])
        print

T = input()
for t in xrange(1,T+1):
    print "Case #%d:" % t
    getPut()
