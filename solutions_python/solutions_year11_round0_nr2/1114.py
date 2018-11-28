import sys
import StringIO


test = StringIO.StringIO("""5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW""")

def format(l):
    out = '['
    out += ', '.join(l)
    out += ']'
    return out

def run(bases, bases_def, oppos_def, calls):
    """
    bases ['Q', 'R']
    bases_def {'QR': 'I', 'RQ': 'I'}
    oppos_def {}
    calls ['R', 'R', 'Q', 'R']

    
    print "bases %s\nbases_def %s\noppos_def %s\ncalls %s\n" % (
        bases, bases_def, oppos_def, calls)
    """
    L = []
    oppos_seek = []
    oppos_mem = []
    
    for e in calls:
        # will combine?
        if L:
            if e + L[-1] in bases_def:
                el = bases_def[e + L[-1]]
                L.pop()
                L.append(el)
                if len(L) in oppos_mem:
                    # if the last element was part of an opposition, then remove
                    # any memory of that opposition
                    oppos_seek.pop()
                    oppos_mem.pop()
                continue
        # did not combine, will it oppose?
        if e in oppos_seek:
            # clear the list
            L = []
            oppos_seek = []
            oppos_mem = []
            continue
            
        # did not combine or oppse, let's add it
        if e in oppos_def:
            oppos_seek.append(oppos_def[e])
            L.append(e)
            oppos_mem.append(len(L))
        else:
            L.append(e)
    return format(L)


try:
    infile = sys.argv[1]
    f = open(infile,'r')
    fo = open(infile + '.out', 'w')        
except IndexError:
    infile = 'test'
    f = test
    fo = sys.stdout

cases = int(f.readline().strip())
for casenum in range(cases):
    
    stack = [x for x in f.readline().strip().split()]
    n_combs = int(stack.pop(0))
    combs = [stack.pop(0) for x in range(n_combs)]
    bases = []
    bases_def = {}
    for trip in combs:
        bases.append(trip[0])
        bases.append(trip[1])
        bases_def[trip[0] + trip[1]] = trip[2]
        bases_def[trip[1] + trip[0]] = trip[2]
    
    n_oppos = int(stack.pop(0))
    oppos = [stack.pop(0) for x in range(n_oppos)]
    oppos_def = {}
    for pair in oppos:
        oppos_def[pair[0]] = pair[1]
        oppos_def[pair[1]] = pair[0]
    
    n_calls = int(stack.pop(0))
    calls = [x for x in stack.pop(0)]
    
    res = run(bases, bases_def, oppos_def, calls)
    
    fo.write('Case #%s: %s\n' % (1+casenum, res))
