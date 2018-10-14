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
        N = int(items[0])
        items = items[1:]
        
        locs = {"O":1, "B":1}
        times = {"O":0, "B":0}
        
        for i in xrange(N):
            who = items[0]
            where = int(items[1])
            
            when = max(max(times.values())+1, \
                       times[who] + abs(where - locs[who]) + 1)
            locs[who] = where
            times[who] = when
            
            items = items[2:]
        
        return max(times.values())


j = Jam()

print j.go("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")

#problem = file("A-small-attempt0.in").read()
problem = file("A-large.in").read()
sol = j.go(problem)
file("A.sol",'w').write(sol)