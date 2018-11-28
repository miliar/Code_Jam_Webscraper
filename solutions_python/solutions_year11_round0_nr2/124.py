from sys import argv
from itertools import izip, imap, count, combinations, permutations


def make_formula( fs ):
    formula = {}
    for f in fs:
        formula[ (f[0], f[1]) ] = f[2]
        formula[ (f[1], f[0]) ] = f[2]
    return formula

def make_rival( rs ):
    rival = {}
    for r in rs:
        try:
            rival[ r[0] ].append( r[1] )
        except KeyError:
            rival[ r[0] ] = [ r[1] ]
        try:
            rival[ r[1] ].append( r[0] )
        except KeyError:
            rival[ r[1] ] = [ r[0] ]
    for k in rival:
        rival[k] = frozenset( rival[k] )
    return rival

def has_rival( el, rival ):
    try:
        r1 = rival[ el[-1] ]
        x = len( r1.intersection( el[:-1] ) )
        return (x > 0)
    except KeyError:
        return False

def make_invoke( f, r, inv ):
    el = []
    for i in inv:
        #if el == []:
        #    el.append( i )
        #    continue
        el.append(i)
        while len(el)>=2 :
            if tuple(el[-2:]) in f:
                out = f[ tuple(el[-2:]) ]
                el.pop()
                el[-1] = out
            elif has_rival( el, r ):
                el = []
            else:
                break        
    return el

'''solvecase("0 0 2 EA")
solvecase("1 QRI 0 4 RRQR")
solvecase("1 QFT 1 QF 7 FAQFDFQ")
solvecase("1 EEZ 1 QE 7 QEEEERA")
solvecase("0 1 QW 2 QW")'''

def solvecase( line ):
    line = line.split()
    
    nformula = int( line[0] )
    formula = make_formula( line[ 1: 1 + nformula ] )
    line = line[ 1 + nformula: ]
    
    nrival = int( line[0] )
    rival = make_rival( line[ 1: 1 + nrival ] )
    line = line[ 1 + nrival: ]
    
    ninvoke = int(line[0])
    invoke = line[1]
    return make_invoke( formula, rival, invoke )


def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        l = inf.readline().strip()
        ans = solvecase( l )
        ans = "[{0}]".format( ", ".join(ans) )
        print "Case #{n}: {ans}".format(n=case, ans=ans)

main()


