import sys



def isint(a):
    return  round(a % 1.0, 2) == 0.0

def doit(N, pd, pg):
    if pg == 0 and pd != 0: return 'Broken'
    if pg == 100 and pd != 100:return 'Broken'
    for D in reversed(range(1, N + 1)):
        wd = D * (pd / 100.0)
        if isint(wd):
            ld = D - wd
            G = D
            wg = G * (pg / 100.0)
            lg = G - wg
            while not isint(wg) or not lg > ld:
                G += 1
                wg = G * (pg / 100.0)
                lg = G - wg
                return 'Possible'
#            return 'D={},G={},wd={},wg={}'.format(D, G, wd, wg)
    return 'Broken'
        


def solve(f):
    f = open(f)
    w = open('out.txt', 'w')
    # Read the number of cases
    T = int(f.readline())
    for t in range(T):
        N, pd, pg = map(int, f.readline().split())
        towrite = 'Case #{}: {}'.format(t + 1, doit(N, pd, pg))
        print towrite
        w.write(towrite + '\n')
    
    f.close()
    w.close()




        
if __name__ == '__main__':
    solve('a-small-attempt2.in')
#    print doit(10, 10, 100)
    
