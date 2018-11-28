#dataset = 'small'
dataset = 'large'

fin = open('A-%s.in' % dataset, 'r')
fout = open('A-%s.out' % dataset, 'w')

def indexOrSize(List, Item):
    try:
        return List.index(Item)
    except ValueError:
        return len(List)

ncases = int(fin.readline())

for i in range(ncases):
    case = i+1
    nengines = int(fin.readline()) # the number of search engines
    engines = list()
    for j in range(nengines):
        engines.append(fin.readline().strip())
    nqueries = int(fin.readline()) # number of queries
    queries = list()
    for j in range(nqueries):
        queries.append(fin.readline().strip())
    
    try:
        answer = 0
        currEng = None
        while queries: # this will actually be interrupted by exception
            lastindex = max([queries.index(eng) for eng in engines if eng])
            answer += 1
            queries = queries[lastindex:]
        print 'exception never raised!'
    except ValueError:
        pass
    
    outputStr = "Case #%d: %d" % (case, answer)
    
    debug = False
    if debug:
        print 'Case #%d:' % case
        for var in ('nengines', 'engines', 'nqueries', 'queries', 'lastindex', 'answer'):
            try: 
                print "\t%s=%s" % (var, eval(var))
            except:
                print 'Some kind of error occurred (%s)' % var
    if not debug:
        print outputStr
    fout.write(outputStr+'\n')

fout.close()