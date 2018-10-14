"""
Finding minimum number of switches between engines to search through given number of queries.
"""

def readFile(fileName):
    return [i.strip() for i in open(fileName).readlines()]

def getEngine(searchengines, queries):
    """
    >>> getEngine(['d', 'g', 'y', 'g'], ['d', 'g'])
    'y'
    >>> getEngine(['d', 'g', 'y'], [])
    'y'
    >>> getEngine(['d', 'g', 'y'], ['d', 'g', 'y'])
    'y'
    >>> getEngine(['d', 'g', 'y'], ['d', 'g', 'y', 'y', 'y','d', 'g', 'd', 'y'])
    'y'
    >>> getEngine(['Yeehaw', 'Yeehaw', 'Googol', 'B9', 'Googol', 'NSM', 'B9', 'NSM', 'Dont Ask', 'Googol'], ['Dont Ask', 'Googol'])
    'Yeehaw'
    """
    res = []
    for q in queries:
        if q in searchengines and q not in res:
            res.append(q)
        if sorted(res) == sorted(searchengines):
            return res[-1]
    if len(res) < len(searchengines):
        return list((set(searchengines)-set(res)))[0] 

def makeTuples(data):
    """Make tuples from file.
    """
    seq = []
    cases = int(data[0])
    caseStarts = 1
    for i in range(cases):
        #Get searchEngine and queries and add that tuple to seq
        enginesCount = int(data[caseStarts])
        enginestarts = caseStarts + 1
        engineEnds = enginestarts+enginesCount-1
        queriesCount = int(data[engineEnds+1])
        queryStarts = engineEnds + 2 
        queryEnds = queryStarts + queriesCount-1
        engines = data[enginestarts:engineEnds+1]
        queries = data[queryStarts:queryEnds+1]
        seq.append((engines, queries))
        caseStarts = queryEnds + 1
    return seq

def getSwitches(engines, queries, switches = 0):
    """It returns all the engine switches by moving through all the queries in list.
    """
    while queries:
        eng = getEngine(engines, queries)
        if eng not in queries:
            return switches
        else:
            index = queries.index(eng)
            return getSwitches(engines, queries[index:], switches+1)
    return switches

def main(data):
    fileData = makeTuples(data)
    f = open(sys.argv[2], 'a')
    for index in range(len(fileData)):
        s, q = fileData[index]  #SearcgEngine, queue
        f.write("Case #%s: %s\n"%(index+1, getSwitches(s, q)))

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    import sys
    main(readFile(sys.argv[1]))
