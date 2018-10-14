# All print statements are entirely debug:
# the final output is in the form of file, *.in
stuff = open('B-small-attempt1.in','rU')
output = open('B-small-out.in','w')
lineState = 0
base = list('QWERASDF')
#print base, 'is base'
caseCount = 1 #for final output

def CombineC(x,y): #inputs should bechars
    ordered = ''.join([x,y])
    reverse = ''.join([y,x])
    if ordered in combine or reverse in combine:
        if ordered in combine:
            return combine[ordered]
        if reverse in combine:
            return combine[reverse]
    else: return False

def OpposeC(x):
    for pair in opposed: #used to return respective item
        if x == pair[0]:
            return pair[1]
        elif x == pair[1]:
            return pair[0]
    else: return False
    
    
for line in stuff: #doing it all line by line
    if lineState == 0:
        cases = int(line)
        lineState = 1
        #print cases, 'number of cases' #debug
        continue
    elif lineState == 1:
        raw = line.split() #think of a better name?
        #print raw # debug
    cInt = int(raw[0])
    invoker = list(raw[-1])

    #print cInt, 'is c' # debug
    #arb = 1 #counter
    combine = {} #changing to DICTIONARY #DONE
    for case in range(1,cInt+1):
        #foo = list(raw[case])
        key = (raw[case])[0:2]
        value = (raw[case])[2]
        combine[key] = value
    #print combine, 'is combine'
    for case in range(0,cInt+1):
        raw.remove(raw[0])
    #print raw, 'is raw no 2'

    #Make the list/dict for opposing
    #Should this be an index/dict instead?
    rInt = int(raw[0]) #REDOING, MAKE SUB LISTS
    #print rInt, 'is rInt'
    opposed = [] #dictionary time DOESN'T NEED DICT
    for case in range(1,rInt+1):
        #opposed.append(raw[case])
        temp = raw[case]
        opposed.append([temp[0],temp[1]])
    #print opposed, 'is opposed'
    for case in range(0,rInt+1):
        raw.remove(raw[0])
    #print raw, 'is raw no 3'

    #ACTUAL HARD PART
    #warning, note differences between invoked and invoker
    #misread opposed element behaviour, CHANGING
    #print invoker, 'is invoker'
    invoked = []
    nInt = int(raw[0])
    #conflict = 0
    #unresolved = [] #NEW: keeps a running count on those which would cause BOOM
    conflict = False

    for thing in invoker: # used to be range(0,nInt)
        invoked.append(thing)
        current = invoked[-1]
        if len(invoked) < 2:
            continue
        
        previous = invoked[-2]
        lolCount = CombineC(previous,current)

        if lolCount != False: # for combining
            del invoked[-1]
            del invoked[-1]
            invoked.append(lolCount)
            continue
        
        fooCount = OpposeC(current) #if it opposes OH CRAP
        if fooCount != False: #what of nested conflicts? NVM, kills ALL
            if fooCount in invoked:
##                if conflict == False: #means both exist
##                    conflict = True
                invoked = [] #deletion
                continue
            else:
                pass
    
    if caseCount == 1:
        output.write('Case #'+str(caseCount)+': ['+', '.join(invoked)+']')
    else: output.write('\n'+'Case #'+str(caseCount)+': ['+', '.join(invoked)+']')
    #print output, 'is invoked no', caseCount
    caseCount += 1

output.close()
