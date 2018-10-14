def do(line):
    # parse the line
    tokens = line.split()
    
    convert = dict()
    numConverts = int(tokens[0])
    for i in xrange(numConverts):
        current = tokens[i + 1]
        convert[current[0:2]] = current[2]
    
    opposed = dict()
    numOpposed = int(tokens[numConverts + 1])
    x = numConverts + 2
    for i in xrange(numOpposed):
        current = tokens[x + i]
        key, val = current[0], current[1]
        if key not in opposed:
            opposed[key] = set()
        opposed[key].add(val)
        if val not in opposed:
            opposed[val] = set()
        opposed[val].add(key)
    
    # do it
    
    answerlist = []
    answerset = set()
    numOccurences = dict()
    
    serie = tokens[-1]
    answerlist.append(serie[0])
    answerset.add((serie[0]))
    numOccurences[serie[0]] = 1
    
    i = 1
    while i < len(serie):
        if len(answerlist) < 1:
            elm = serie[i]
            answerlist.append(elm)
            answerset.add(elm)
            numOccurences[elm] = 1
            i = i + 1
            continue
        prev, curr = answerlist[-1], serie[i]
        if curr + prev in convert:
            newelement = convert[curr + prev]
            answerlist[-1] = newelement
            numOccurences[prev] = numOccurences[prev] - 1
            if numOccurences[prev] < 1:
                del numOccurences[prev]
                answerset.discard(prev)
            answerset.add(newelement)
            if newelement in numOccurences:
                numOccurences[newelement] = numOccurences[newelement] + 1
            else:
                numOccurences[newelement] = 1
        elif prev + curr in convert:
            newelement = convert[prev + curr]
            answerlist[-1] = newelement
            numOccurences[prev] = numOccurences[prev] - 1
            if numOccurences[prev] < 1:
                del numOccurences[prev]
                answerset.discard(prev)
            answerset.add(newelement)
            if newelement in numOccurences:
                numOccurences[newelement] = numOccurences[newelement] + 1
            else:
                numOccurences[newelement] = 1
        elif (curr in opposed and len(opposed[curr].intersection(answerset)) > 0) or \
             (prev in opposed and len(opposed[prev].intersection(answerset)) > 0):
            answerlist = []
            answerset = set()
            numOccurences = dict()
        else:
            answerlist.append(curr)
            answerset.add(curr)
            if curr in numOccurences:
                numOccurences[curr] = numOccurences[curr] + 1
            else:
                numOccurences[curr] = 1
        
        i = i + 1
    
    return '[]' if len(answerlist) == 0 else \
            str(answerlist).replace('\'', '')
    

def go():
    print do("1 QEN 1 AQ 10 AWAREEQESS")
    
    try:
        inp = open('C:/Users/mrt/Desktop/B-large.in', 'r')
        out = open('C:/Users/mrt/Desktop/b-large.out', 'w')
        numCases = inp.readline()
        numCases = numCases.strip('\n\r')
        numCases = int(numCases)
        for i in xrange(numCases):
            line = inp.readline()
            line = line.strip('\n\r')
            answer = do(line)
            out.write('Case #' + str(i + 1) + ': ' + answer + '\n')
        inp.close()
        out.close()
        print 'done'
    except:
        print 'hmm'

go()
