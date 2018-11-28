'''
Created on May 7, 2011

@author: yonch
'''

class Jam(object):
    '''
    One Problem
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
        pass
    
    def go(self, problemText, isSingleLine = True):
        lines = problemText.splitlines()
        numCases = int(lines[0])
        
        if isSingleLine:
            resList = []
            for i in xrange(numCases):
                resList.append("Case #%d: %s" % (i+1, self.goOne(lines[1+i])))
            res = "\n".join(resList)
        else:
            assert(False)
        
        return res
    
    def goOne(self, problem):
        items = problem.split(" ")
        #deriv
        C = int(items[0])
        items = items[1:]
        deriv = {}
        for i in xrange(C):
            x = items[i]
            deriv[x[0]+x[1]] = x[2]
            deriv[x[1]+x[0]] = x[2]
        items = items[C:]
        
        # conflict
        D = int(items[0])
        items=items[1:]
        conf = {}
        for i in xrange(D):
            x = items[i]
            conf.setdefault(x[0],[]).append(x[1])
            conf.setdefault(x[1],[]).append(x[0])
        items = items[D:]
        
        elems = []
        conflicts = set()
        N = int(items[0])
        s = items[1]
        for i in xrange(N):
            c = s[i]
            elems.append(c)
            if len(elems) >= 2 and deriv.has_key(elems[-2] + elems[-1]):
                elems = elems[:-2] + [deriv[elems[-2] + elems[-1]]]
            else:
                if set(elems).intersection(set(conf.get(c,[]))) != set():
                    conflicts = set()
                    elems = []
        
        return "[%s]" % (", ".join(elems))
                
        

j = Jam()

print j.go("""5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW""")

if 1:
    #problem = file("B-small-attempt0.in").read()
    problem = file("B-large.in").read()
    sol = j.go(problem)
    file("A.sol",'w').write(sol)