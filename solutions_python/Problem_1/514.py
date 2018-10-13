
class Case:    
    def __init__(self, id):
        self.id = id
        self.engines = []
        self.queries = []
        self.switches = -1
        
    def solve(self, fp):
        print "Current Case #%d, S:%d Q:%d" % (self.id, len(self.engines), len(self.queries))                        
        
        self.switches = self.fast_count_switches(self.queries)

        fp.write("Case #%d: %d\n" % (self.id, self.switches))
        print "Case #%d: %d" % (self.id, self.switches)
                               
    def fast_count_switches(self, queries):
        
        def _reset_engines(edict):
            for e in self.engines: 
                edict[e] = False
                
        def _need_to_switch(edict):
            for val in edict.values():
                if not val:
                    return False
                    
            return True
                    
        cur = dict()
        _reset_engines(cur)
        sequence = []
        
        switches = 0
        for (ind, q) in list(enumerate(queries)):
            if q in cur:
                # name of engine
                if cur[q]:
                    # already not our choice
                    continue
                
                cur[q] = True
                if _need_to_switch(cur):
                    switches += 1
                    sequence.append(q)
                    _reset_engines(cur)
                    cur[q] = True                
                
                
            continue
            
        # last one
        for (key,val) in cur.iteritems():
            if val == 0:
                sequence.append(key)
                break
        
        print "Engine sequence: %s" % (",".join(sequence))
        return switches
    
def read_problem(filename):
    
    f = open(filename)
    num_cases = int(f.readline())
    cases = []
    for i in range(num_cases):
        num_engines = int(f.readline())
        c = Case(i+1)
        c.engines = []
        for dummy in range(num_engines):
            c.engines.append(f.readline().strip())
        
        num_queries = int(f.readline())
        for dummy in range(num_queries):
            c.queries.append(f.readline().strip())
        cases.append(c)
        
    return cases
    

# **************    
#     MAIN
# **************

fo = open("out.txt","w")
for case in read_problem("A-large.in"):
    case.solve(fo)
