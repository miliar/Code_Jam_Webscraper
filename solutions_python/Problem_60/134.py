import re
from sys import argv
#from dg import trace
zrl = lambda xs: zip(range(len(xs)), xs)


def seperate_them(B, D, chicks):
    goods, bads = [], []
    for c in chicks:
        if B - c[0] <= c[1] * D:
            goods.append(c)
        else:
            bads.append(c)
    return goods, bads


def minswaps (B, D, chicks, desired):
    winners, stragglers = seperate_them(B, D, chicks)

    @memoize
    def enemies (w):
        return len([s for s in stragglers if s[0] >= w[0]])
        
    best_winners = sorted(winners, key=enemies)
    if len(best_winners) < desired:
        return None
    else:
        return sum([enemies(w) for w in best_winners[:desired]])
    
def memoize(f):
    cache = {}
    def real_f(*args):
        def do_the_work ():
            product = f(*args)
            cache[tuple(args)] = product
            return product
        return cache.get(tuple(args), do_the_work())
    return real_f

def parse_ints(count, line):
    gs = ('''(\d+)''',) * count
    expr = '''^\s*''' + ('''\s*'''.join(gs)) + '''\s*$'''
    m = re.search(expr, line)
    return [int(x) for x in m.groups()]

lines = open(argv[1], 'r').readlines()
casecount = int(re.search('''^\s*(\d+)\s*$''', lines[0]).group(1))

i = 1
casesprocessed = 0
while i < len(lines):
    cBirds, rBirds, barn, deadline = parse_ints(4, lines[i])
    positions = parse_ints(cBirds, lines[i+1])
    speeds    = parse_ints(cBirds, lines[i+2])
    birds = zip (positions, speeds)

    i += 3 # consumed!
    casesprocessed += 1
    swaps = minswaps(barn, deadline, birds, rBirds)
    if swaps == None:
        print "Case #%d: IMPOSSIBLE" % (casesprocessed,)
    else:
        print "Case #%d: %d" % (casesprocessed, swaps)

