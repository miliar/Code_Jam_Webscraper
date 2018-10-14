import sys

###############################################################################
# Helper functions                                                            #
###############################################################################
def handleCase(case,dic):
    matchDic = dic.copy()
    combi = False;
    i = 0
    combiSet = []
    for c in case:
        if not combi and c == '(':
            combi = True
        elif combi and c == ')':
            for word in dic:
                ok = False
                for d in combiSet:
                    if word[i] == d:
                        ok = True
                if not ok and (word in matchDic):
                    matchDic.remove(word)            

            combi = False
            combiSet = []
            i += 1
        elif combi:
            combiSet.append(c)
        else:
            for word in dic:
                if not(word[i] == c) and (word in matchDic):
                    matchDic.remove(word)

            i += 1

    return [len(matchDic),matchDic]
      


###############################################################################
# Main                                                                        #
###############################################################################
input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
debug  = open(sys.argv[1].replace('in','debug'),'w')

# Read header
tmp = input.readline().strip().split()
nWords = int(tmp[1])
nCases = int(tmp[2])

# Read dictionary
dic = set([])
for i in range(nWords):
    dic.add(input.readline().strip())
assert len(dic) == nWords

# Handle cases
results = []
for i in range(nCases):
    case = input.readline().strip()
    [res,matchDic] = handleCase(case,dic)
    print "Case # " + str(i+1) + ": " + str(res)
    output.write("Case #" + str(i+1) + ": " + str(res) + "\r\n")

    #debug.write("Case #" + str(i+1) + ": " + str(res) + "\r\n")
    #debug.write(case + "\r\n")
    #debug.write("Matching:     " + str(matchDic) + "\r\n")
    #debug.write("Not-matching: " + str(dic.difference(matchDic)) + "\r\n")

    results.append(res)
    



