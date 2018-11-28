import copy

def solve(dataset):
    datafile = open(dataset, 'r')
    outfile = open("c:/temp/results.txt",'w')
    
    numberoftestcases = int(datafile.readline().strip())
    print "Number of Test Cases = %d" % (numberoftestcases)
    for testcasenumber in range(1,numberoftestcases+1):
        print "Test case #%d" % (testcasenumber)
        numberofsearchengines = int(datafile.readline().strip())
        print "%d search engines:" % (numberofsearchengines)
        searchengines = []
        for se in xrange(0,numberofsearchengines):
            searchengines.append(datafile.readline().strip('\n'))
        print repr(searchengines)

        numberofsearchs = int(datafile.readline().strip())
        print "%d searches:" % (numberofsearchs)
        searches = []
        for se in xrange(0,numberofsearchs):
            searches.append(datafile.readline().strip('\n'))
        print repr(searches)

        answer = solvecase(searchengines,searches)
        print "Case #%d: %d" % (testcasenumber, answer)
        outfile.write("Case #%d: %d\n" % (testcasenumber, answer))

class numeric_compare:
    def __init__(self):
        self.countdic = None
    def setcounts(self, newcounts):
        self.countdic = newcounts
    def comparecounts(self,x,y):
        if self.countdic[x] > self.countdic[y]:
            return 1
        elif self.countdic[x] == self.countdic[y]:
            return 0
        else:
            return -1

comp = numeric_compare()

def get_next_switch(current_pos, searches, numengines):
    engine_watch = {}
    numseen = 0

    while(numseen<numengines and current_pos < len(searches)):
      
        if searches[current_pos] not in engine_watch:
            numseen = numseen + 1
            engine_watch[searches[current_pos]] = True

        if numseen<numengines:
            current_pos = current_pos + 1

    return current_pos
        

def solvecase(searchengines, searches):
    switches = []
    engines = {}
    
    for engine in searchengines:
        if engine in engines:
            print "Duplicate engine"
        else:
            engines[engine] = 0

    for search in searches:
        if search not in engines:
            print "unrecognizable search"

    numswitches = 0
    current_engine = None

    initial_pos = get_next_switch(0, searches, len(searchengines))
    if initial_pos >= len(searches):
        return 0

    #otherwise set our initial search engine choice:
    current_engine = searches[initial_pos]
    print "Starting with engine: %s" % (current_engine)
    current_pos = initial_pos

    while(current_pos < len(searches)):
        numswitches = numswitches + 1
        next_pos = get_next_switch(current_pos, searches, len(searchengines))
        if next_pos < len(searches):
            next_engine = searches[next_pos]
        else:
            next_engine = "Possibly different options"
        print "Switching to engine: %s @ #%d" % (next_engine, current_pos)
        current_pos = next_pos
        
    return numswitches
