import sys


def saving(filename):
    f = open(filename,'rb')
    line = f.readline()
    N = int(line.rstrip()) # N is the number of test cases
##    print 'Test Case Number: ' + str(N)
    results = []
    for i in range(N):
##        print 'Test Case '+str(i+1)+':'
        SwitchTimes = 0
        Engines = []
        EnginesIn = []
        Queries = []
        S = int(f.readline().rstrip()) # S is the number of search engines
##        print 'Search Engine Number: ' + str(S)
        for j in range(S):
            Engines.append(f.readline().rstrip())
            EnginesIn.append(False)
##        print Engines
        Q = int(f.readline().rstrip()) # Q is the number of queries
##        print 'Query Number: ' + str(Q)
        for j in range(Q):
            Queries.append(f.readline().rstrip())
##        print Queries
        for QueryItem in Queries:
            if QueryItem in Engines:
                EnginesIn[Engines.index(QueryItem)] = True
                if False not in EnginesIn:
                    SwitchTimes += 1
                    EnginesIn = [False for flag in EnginesIn]
                    EnginesIn[Engines.index(QueryItem)] = True
        results.append(SwitchTimes)
##    print 'Results: '
    k = 1
    for result in results:
        print 'Case #'+ str(k)+': '+str(result)
        k+=1
    f.close()



if __name__ == '__main__':
    saving(sys.argv[1])
