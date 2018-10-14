import sys
from itertools import count, izip

def main():
    file = open("A-large.in")
    output = open("A-large.out", "w")
    numCases = int(file.readline())
    for case in range(numCases):
        numSearchEngines = int(file.readline())
        searchEngines = dict()
        for i in range(numSearchEngines):
            searchEngines[file.readline()] = i
        
        numQueries = int(file.readline())
        queries = []
        if numQueries < 1:
            output.write("Case #" + str(case+1) + ": 0\n")
            continue
        for j in range(numQueries):
            queries.append(file.readline())
        
        #set up the memoizatoin array
        memoizationArr = []
        memoizationArr.append([0 for i in range(numSearchEngines)])
        memoizationArr[0][searchEngines[queries[0]]] = sys.maxint
        for i in range(1, numQueries):
            minvalue = min(memoizationArr[i-1]) 
            memoizationArr.append([minvalue+1 for j in range(numSearchEngines)])
            for k in range(numSearchEngines):
                if memoizationArr[i-1][k] < memoizationArr[i][k]:
                    memoizationArr[i][k] = memoizationArr[i-1][k]
            memoizationArr[i][searchEngines[queries[i]]] = sys.maxint
                             
        output.write("Case #" + str(case+1) + ": "
                     + str(min(memoizationArr[numQueries-1])) + "\n")

if __name__ == "__main__":
    main()
