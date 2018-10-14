




def next_perm(p):
    if len(p) == 1:
        return None
        
    n = next_perm(p[1:])
    if n:
        return [p[0]] + n
    else:
        p2 = sorted(p)
        i = p2.index(p[0])
        
        for i in range(len(p2)):
            if p2[i] > p[0]:
                break
        else:
            return None
        return [p2[i]] + p2[:i] + p2[i+1:]


def next_num(n):
    n2 = next_perm(n)
    if n2:
        return n2
    nzeroes = n.count(0)
    n2 = [d for d in n if d != 0]
    n2.sort()
    n2 = [n2[0]] + ([0] * (nzeroes+1)) + n2[1:]
    return n2
            
T = int(raw_input())
for ncase in range(T):
    N = map(int, raw_input().strip())
    print 'Case #%d: %s' % ((ncase+1), ''.join(map(str, next_num(N)))) 
    