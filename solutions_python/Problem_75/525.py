f = open('B-large.in')
x = f.readlines()
x.pop(0)


def processInput(input):
    
    numcs = int(input[0])
    input.pop(0)
    compounds = {}
    while numcs:
        rule = input[0]
        compounds["%s%s" % (rule[1],rule[0])] = rule[2]
        compounds["%s%s" % (rule[0],rule[1])] = rule[2]
        numcs -=1
        input.pop(0)

    opposed = {}

    numos = int(input[0])
    input.pop(0)
    while numos:
        rule = input[0]
        if not rule[1] in opposed:
            opposed[rule[1]] = []
        if not rule[0] in opposed:
            opposed[rule[0]] = []
        opposed[rule[1]].append(rule[0])
        opposed[rule[0]].append(rule[1])

        numos -=1
        input.pop(0)
    input.pop(0)
    sequence = input[0]
    return compounds,opposed,sequence


def checkopposed(letter, opposed, elist):
    if opposed.has_key(letter):
        checkletters = opposed[letter]
       
        for x in checkletters: 
            if x in elist:
                return True

    return False

    

i = 0
for line in x:
    i+=1
    g = line.split()
    compounds, opposed, sequence = processInput(g)


    elist = []
    while len(sequence):
        letter = sequence[0]
        sequence  = sequence[1:]
        if len(elist): 
            lastletter = elist[len(elist)-1] 

            #check compounds
            checkkey = ("%s%s" % (lastletter,letter))
            if checkkey in compounds:
                elist.pop()
                letter = compounds[checkkey] 

        if checkopposed(letter,opposed,elist):
            elist = []
            letter = None

        #check opposed  
        if letter: 
            elist.append(letter)

        #print
        #print
        #print elist
    print "Case #%d: [%s]" % (i,', '.join(elist))
