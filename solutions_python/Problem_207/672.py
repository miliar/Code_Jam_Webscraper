constraints = {
    'R' : ['R', 'O', 'V'],
    'O' : ['O', 'R', 'Y'],
    'Y' : ['Y', 'O', 'G'],
    'G' : ['G', 'Y', 'B'],
    'B' : ['B', 'G', 'V'],
    'V' : ['V', 'B', 'R'],
}

def do_case(i):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    pon = [['R',R], ['O',O], ['Y',Y], ['G',G], ['B',B], ['V',V]]

    #hpon = {
    #    'R': R,
    #    'O': O,
    #    'Y': Y,
    #    'G': G,
    #    'B': B,
    #    'V': V,
    #}
    
    rvb = {
        'R': R+O+V,
        'Y': Y+O+G,
        'B': B+G+V,
    }
    
    elems = {
        'R': ['R'],
        'O': ['R', 'Y'],
        'Y': ['Y'],
        'G': ['Y', 'B'],
        'B': ['B'],
        'V': ['B', 'R'],
    }
    
    
    rv = []
    last = None
    first = None
    for j in xrange(N):

        def mycomp(a, b):
            ma = max(rvb[e] for e in elems[a[0]])
            mb = max(rvb[e] for e in elems[b[0]])
            if ma < mb:
                #print "ma < mb", ma, mb
                return -1
            if ma > mb:
                #print "ma > mb", ma, mb
                return 1
            if a[1] < b[1]:
                #print "a[1] < b[1]", a[1], b[1]
                return -1
            if a[1] > b[1]:
                #print "a[1] > b[1]", a[1], b[1]
                return 1
            if first in elems[a[0]] and first not in elems[b[0]]:
                return 1
            if first in elems[b[0]] and first not in elems[a[0]]:
                return -1
            return 0

        s = sorted(pon, reverse=True, cmp = mycomp)
        #print "**", s
        #print "++", rvb
        
        flag = True
        while flag:
            col = s[0][0]
            if last in constraints[col]:
                s.pop(0)
                continue
            flag = False

        if s[0][1] == 0:
            rv = list('IMPOSSIBLE')
            break
        rv.append(s[0][0])
        if not first:
            first = s[0][0]
            
        #print rv
        last = s[0][0]
        s[0][1] -= 1
        for e in elems[s[0][0]]:
            rvb[e] -= 1

    if rv != list('IMPOSSIBLE'):
        if rv[0] in constraints[rv[N-1]]:
            rv = list('IMPOSSIBLE')
        
    print "Case #{}: {}".format(i+1, ''.join(rv))

def main():
    N = int(raw_input())
    for i in xrange(N):
        do_case(i)

main()

