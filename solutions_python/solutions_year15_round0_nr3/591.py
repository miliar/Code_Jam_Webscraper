TABLE = [['1',  'i',  'j',  'k' ],
         ['i',  '-1', 'k',  '-j'],
         ['j',  '-k', '-1', 'i' ],
         ['k',  'j',  '-i', '-1']]


def factor(s):
    return '-' * (s.count('-') % 2) + s[-1] 


DCT = {(sa + a, sb + b): factor(sa + sb + TABLE[i][j])
       for i, a in enumerate(TABLE[0])
       for j, b in enumerate(TABLE[0])
       for sa in ('','-')
       for sb in ('','-')}


VALUES = set(DCT.values())


def mul(a, b):
    return DCT[a, b]


def red(s):
    return reduce(mul, s, '1')

def gen(s, v, r=False):
    prev = '1'
    for i, x in enumerate(s):
        if prev == v:
            yield i
        prev = mul(x, prev) if r else mul(prev, x)
        

def solve(s):
    ks = list(gen(s[::-1], 'k', r=True))
    for i in gen(s, 'i'):
        for j in gen(s[i:], 'j'):
            if len(s) - i - j in ks:
                return True
    return False


def parse(fname):
    with open(fname) as f:
        next(f)
        for line in f:
            n = int(line.split()[1])
            yield next(f).strip() * n
            

        
def display(i, r):
    r = ("NO", "YES")[r]
    print "Case #{}: {}".format(i, r)


def solve_file(fname):
    for i, s in enumerate(parse(fname), 1):
        display(i, solve(s))

 
if __name__ == "__main__":
    import sys
    solve_file(sys.argv[1])




