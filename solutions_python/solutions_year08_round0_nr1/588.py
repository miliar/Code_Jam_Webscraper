#!/usr/bin/python

infilename = "A-large.in"
outfilename = "out.txt"

class Query_Set:
    def __init__(self, engines):
        self.queries = []
        self.enginesearches = {}
        self.engines = engines
    def which_to_use(self):
        unused = [engine for engine in self.engines]
        while len(self.queries) > 0 and len(unused) > 1:
            print("Queries = " + str(self.queries))
            query = self.queries.pop(0)
            if query in unused:
                unused.remove(query)
            print("Unused = " + str(unused))
        if unused[0] in self.queries:
            went_until = self.queries.index(unused[0])
        else:
            went_until = len(self.queries)
        self.queries = self.queries[went_until:]
        print("Now we're at " + str(self.queries))
        return unused[0]
    def num_switches(self):
        first_engine = self.which_to_use()
        print("Started with " + str(first_engine))
        times_switched = 0
        while len(self.queries) > 0:
            times_switched = times_switched + 1
            switched_to = self.which_to_use()
            print("Switch #" + str(times_switched) + ": " + str(switched_to))
        return times_switched
    
infile = open(infilename)
outfile = open(outfilename, "w")
num_cases = int(infile.readline().strip())

for case in range(1, num_cases+1):
    num_engines = int(infile.readline().strip())
    engines = []
    for engine_num in range(num_engines):
        engines.append(infile.readline().strip())
    this_set = Query_Set(engines)
    num_queries = int(infile.readline().strip())
    for i in range(num_queries):
        this_set.queries.append(infile.readline().strip())
    num_switches = this_set.num_switches()
    outfile.write("Case #" + str(case) + ": " + str(num_switches) + "\n")

outfile.close()
    
