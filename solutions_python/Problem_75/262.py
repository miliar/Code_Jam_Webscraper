import sys,math

numOfTests= int(sys.stdin.readline())
for t in range(1,numOfTests+1):
    result =""
    line = sys.stdin.readline().split()
    com = []
    opp = []
    inv = []
    
    #use dictionary for fast look up
    C = dict()
    newC = dict()
    O = dict()
    I = dict()
    
    combine = int(line[0])
    if combine != 0:
        com = line[1:combine+1]
        for c in com:
            C[c[0]] = c[1]  #combine with
            C[c[1]] = c[0]
            newC[c[0]] = c[2] #combine to form
            newC[c[1]] = c[2]
    oppose = int(line[combine+1])
    if oppose != 0:
        opp = line[2+combine:2+combine+oppose]
        for o in opp:
            O[o[0]] = o[1]#opposed to
            O[o[1]] = o[0]
            
    invoke = int(line[combine+oppose+2])
    inv = line[3+combine+oppose]
    
    #count number of element
    eleCount = dict()
    for o in opp:
        eleCount[o[0]]=0
        eleCount[o[1]]=0
    
    last = ''
    for i in inv:
        #combine
        if i in C.keys() and C[i] == last:
            last = newC[i]
            if C[i] in eleCount.keys():
                eleCount[C[i]] = eleCount[C[i]] - 1
            result = result[0:len(result)-1] + newC[i]
            continue
        
        #oppose
        if i in O.keys() and eleCount[O[i]] > 0:
            last = ''
            result = ""
            for o in opp:
                eleCount[o[0]]=0
                eleCount[o[1]]=0
            continue    
        
        #nothing
        if i in eleCount.keys():
            eleCount[i] = eleCount[i]+1
        last = i
        result = result + i
    if (len(result) != 0):
        resString = ""
        resString = "Case #" +str(t)+": [" + result[0]
        for i in result[1:len(result)-1]:
            resString = resString + ", " + i
        if len(result) != 1:
            resString = resString + ", " + result[len(result)-1] + "]"
        else:
            resString = resString + "]"
        print resString
    else:
        print "Case #" +str(t)+": []"
    