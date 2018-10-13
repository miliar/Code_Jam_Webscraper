class Case(object):
    
    def __init__(self, file):
        self.num_engines = int(file.readline())
        self.engines = [ file.readline() 
                            for cnt in xrange(self.num_engines) ]
        self.num_queries = int(file.readline())
        
        self.queries = [ file.readline() 
                            for cnt in xrange(self.num_queries) ]
        self.num_switches = 0
        
    def get_best_greedy(self, from_index):
        
        encountered = {}
        for engine in self.engines:
            encountered[engine] = False
        best = [ engine 
                    for engine in self.engines ]
        
        for queryindex in xrange(from_index, len(self.queries)):
            query = self.queries[queryindex]
            if query in encountered and not encountered[query]:
                encountered[query] = True
                if len(best) == 1:
                    break
                else:
                    best.remove(query)
        #print "best to use from index %d is %s" % (from_index, best[0])
        return best[0]
    
    def solve(self):
        queryindex = 0
        
        engines = {}
        for engine in self.engines:
            engines[engine] = True
            
        current = self.get_best_greedy(queryindex)
        for query in self.queries:
            if query == current:
                current = self.get_best_greedy(queryindex)
                self.num_switches += 1
            
            queryindex+= 1 
        # greedy pick the engine which can be used the most
        # times since "last switch" 
        
        return self.num_switches

if __name__ == '__main__':
    
    file = 'test.txt'
    file = 'A-large.in'
    fp = open(file, 'rb')
    num_cases = int(fp.readline())
    
    cases = [ Case(fp)  
                for x in xrange(num_cases) ]
#    print cases[6].solve()
    for case_index in xrange(len(cases)):
        print "Case #%d: %d" % (case_index + 1, cases[case_index].solve())