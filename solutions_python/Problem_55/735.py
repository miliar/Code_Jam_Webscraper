import re
from sys import argv
#from dg import trace
zrl = lambda xs: zip(range(len(xs)), xs)

def coaster(rides, kapacity, cliques):
    firstclique = 0
    money = 0
    cache = {}
    while rides != 0:
        rides -= 1
        folks_served, cliques_served = serve(kapacity, firstclique, firstclique, cliques, cache)
        assert folks_served > 0
        assert cliques_served > 0
        money += folks_served
        firstclique = (firstclique + cliques_served) % len(cliques)
    return money



#@trace
def serve (kapacity, firstclique, boundary, cliques, cache):
    result = cache.get((kapacity,firstclique), None)
    if result == None:
        if kapacity >= cliques[firstclique]:
            nextclique = (firstclique+1)%len(cliques)
            if nextclique == boundary:
                result = cliques[firstclique], 1
            else:
                fs, cs = serve(kapacity - cliques[firstclique],
                               nextclique,
                               boundary,
                               cliques,
                               cache)
                result = (fs+cliques[firstclique], 1+cs)
                cache[(kapacity, firstclique)] = result
                
        else: # base case
            result = 0, 0
    return result
        
        



def pairs(xs):
    assert (len(xs) % 2) == 0 # can't make pairs out of odd number of elements!
    return zip(xs[::2], xs[1::2])

def main ():
    lines = open(argv[1], 'r').readlines()
    casecount = int(re.search('''^\s*(\d+)\s*$''', lines[0]).group(1))
    cases = pairs(lines[1:])
    for i, case in zrl(cases):
        groups = re.search('''^\s*(\d+)\s*(\d+)\s*(\d+)\s*$''', case[0]).groups()
        cliques = [int(m.group(1)) for m in re.finditer('''\s*(\d+)(\s|$)''', case[1])]
        r, k, n = [int(x) for x in groups]
        cliques = tuple(cliques[:n])
        
        print "Case #%d: %s" % (i+1, coaster(r, k, cliques))


if __name__=='__main__': main()

