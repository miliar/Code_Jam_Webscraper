import sys

def universe(engines,searches):
    if len(searches) == 0 or len(engines) == 0:
        return 0
    current_engine = 0
    table = []
    for i in range(0,len(engines)):
        table.append(0)
    if contains(searches[0],engines):
        table[engines.index(searches[0])] = sys.maxint
    
    for i in range(1,len(searches)):
        temp = []
        for j in range(0,len(engines)):
            # let's not destroy the universe...
            if engines[j] == searches[i]:
                temp.append(sys.maxint)
            else:
                possibles = table[:]
                for k in range(0,len(possibles)):
                    possibles[k] += 1
                possibles[j] -= 1                    
                temp.append(min(possibles))
        table = temp
        #print table
    return min(table)

def contains(element,elements):
    try:
        elements.index(element)
        return True
    except:
        return False

n = int(raw_input())
for i in range (1,n+1):
    num_engines = int(raw_input())
    engines = []
    for j in range(0,num_engines):
        engines.append(raw_input())
    num_searches = int(raw_input())
    searches = []
    for j in range(0,num_searches):
        searches.append(raw_input())
    print "Case #%d: %d"% (i,universe(engines,searches))
    
