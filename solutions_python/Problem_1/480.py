import sys
sys.setrecursionlimit(10000)

""" CodeJam 1 - Saving the Universe """
def saviour(engines, queries):
    """ Function to save a universe """
    if len(queries) == 0 :
        return 0

    indices = []
    for engine in engines:
        try:
            indices.append(queries.index(engine))
        except ValueError:
            return 0
        
    return saviour(engines, queries[max(indices):]) + 1


INPUT = open('input', 'r')
OUTPUT = open('output', 'w')

for j in xrange(int(INPUT.readline())):
    engine_list = []
        
    for i in xrange(int(INPUT.readline())):
        engine_list.append(INPUT.readline())
            
    query_list = []
        
    for i in xrange(int(INPUT.readline())):
        query_list.append((INPUT.readline()))
        
    OUTPUT.write("Case #%d: %d\n" % (j+1, saviour(engine_list, query_list)))
