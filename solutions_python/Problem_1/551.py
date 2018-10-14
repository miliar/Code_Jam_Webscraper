def get_switches(searchengine, remainingqueries):
    #print "%s:%s" % (searchengine,remainingqueries)
    if remainingqueries == []:
        return 0
    i = 0
    switches = 0
    while(i != len(remainingqueries)):
        if(searchengine == remainingqueries[i]):
            break
        else:
            i = i+1
            
    if(i == len(remainingqueries)):
        return 0
    else:
        '''find search engine with smallest swtiches from here'''
        resultswitches = []
        for j in searchengines:
            if(j != searchengine and j != remainingqueries[i]):
                resultswitches.append(1+get_switches(j,remainingqueries[i:]))

        resultswitches.sort()
        #print resultswitches
        return resultswitches[0]

def get_switches2(searchengines, queries):
    '''
        see how far you can get down with each choice
    '''
    switches = 0
    max = 0
    while(max != len(queries)):
        j = max
        for engine in searchengines:
            i = max
            while(i != len(queries)):
                if(engine == queries[i]):
                    break
                else:
                    i = i+1
            if(i > j):
                j = i
        max = j

        if(max == len(queries)):
            break
        else:
            switches = switches+1
            
    return switches
        
        

f = open("A-large.in")
numcases = int(f.readline())
for case in range(numcases):
    numsearch = int(f.readline())
    searchengines = []
    queries = []
    for i in range(1,numsearch+1):
        searchengines.append(f.readline().strip("\n"))

    numqueries = int(f.readline())
    for i in range(1,numqueries+1):
        queries.append(f.readline().strip("\n"))


    #print searchengines
    #print queries
    #print queries[:]
    if(numqueries == 0 or numsearch == 0):
        print "Case #%s: %s" %(case+1,0)
    else:
        print "Case #%s: %s" %(case+1, get_switches2(searchengines, queries))

'''
start with a search engine that is not the first
in the query

continue until forced to switch,
look one ahead and switch to not that one


'''



    


    
