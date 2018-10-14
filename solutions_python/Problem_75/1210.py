_base_dict = dict()

def generate(inp):
    inp.reverse()
    
    C = int(inp.pop())
    C_D = dict(_base_dict)
    
    for i in xrange(C):
        _t = inp.pop()
        C_D[_t[:2]] = _t[2]
        C_D[_t[:2][::-1]] = _t[2]
    
    D = int(inp.pop())
    D_L = {i: set() for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'}
    for k in xrange(D):
        i = inp.pop()
        D_L[i[0]].add(i[1])
        D_L[i[1]].add(i[0])
    
    N = int(inp.pop())
    N_L = inp.pop()
    
    r = {
        'combine': C_D,
        'oppose': D_L,
        'invoke': N_L
    }
    return r

any_in = lambda a, b: any([i in a for i in b])
last = lambda a: '#' if len(a)==0 else a[-1]
def solved(combine, oppose, invoke):
    r = ''
    for e in invoke:
        _t = ''
        if last(r)+e in combine.keys():
            _t = combine[last(r)+e]
            r = r[:len(r)-1]
        elif any_in(r, oppose[e]):
            r=''
        else:
            _t = e
        r+=_t
    return r

def main():
    N = int(raw_input())
    for i in xrange(N):
        problem = generate(raw_input().split(' '))
        print 'Case #{0}: ['.format(i+1)+(', '.join([c for c in solved(**problem)]))+']'

if __name__=='__main__':
    main()
