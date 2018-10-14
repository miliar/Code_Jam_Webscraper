import sys

def main():
    # read in command-line arguments
    junk, testFile = sys.argv
    
    data = open(testFile,'r').read().splitlines()
    
    N = int(data[0])
    caseNum = 1
    line = 1
    while line < len(data):
        # read number of search engines
        S = int(data[line])
        line += 1
         
        # read search engine names
        engines = data[line:line+S]
        line += S
    
        # read number of queries
        Q = int(data[line])
        line += 1
         
        # extract queries
        queries = data[line:line+Q]
        line += Q
    
        # get down to business
        switches = numSwitches(engines, queries)
        
        print('Case #' + str(caseNum) + ': ' + str(switches))
        caseNum += 1

def numSwitches(engines, queries):
    chunks = 0
    a = 0 # start of group
    while True:
        taboo = {0:len(engines)}
        b = 0
        for b in xrange(a,len(queries)):
             q = queries[b]
             if q not in taboo:
                  taboo[q] = None
                  taboo[0] -= 1
                  if taboo[0] == 0:
                        chunks += 1
                        a = b
                        break            
        if taboo[0] >= 1 or a == len(queries) - 1:
            chunks += 1
            break
    return chunks - 1

if __name__ == "__main__":
    main()
