from operator import itemgetter

def main() :
    numTestCases = int(raw_input())
    for z in range(numTestCases) :
        numSearchEngines = int(raw_input())
        s = []
        for y in range(numSearchEngines) :
            s.append(raw_input())

        d = dict((i, 0) for i in s)

        numQueries = int(raw_input())

        switchCount = 0
        for i in range(numQueries) :
            query = raw_input()
            d[query] += 1
            if all(d[k] > 0 for k in d) :
                switchCount += 1
                d = dict((i, 0) for i in s)
                d[query] += 1

        print "Case #%d: %d" % (z + 1, switchCount)

main()



