f = open('/Users/alarobric/Downloads/B-small-attempt0.in', 'r')
g = open('/Users/alarobric/Downloads/B-small-attempt0.out', 'w')
 
cases = int(f.readline())
#base = {Q, W, E, R, A, S, D, F}

 
for i in range (1, cases + 1):
    line = f.readline().split()
    C = int(line.pop(0))
    print "case", i
    #print C, "combos"
    
    combos = {}
    for j in range(0, C):
    	combo = line[j]
        combos[combo[:2]] = combo[2:]
        
    D = int(line[C])
    #print "D",D
    opposed = {}
    for j in range(1, D+1):
    	opp = line[C+j]
        opposed[opp[0]]=opp[1]
        opposed[opp[1]]=opp[0]
    
    print "combos", combos    
    print "opposed", opposed
    N = int(line[C+D+1])
    #print "N", N
    instr = line[C+D+2]
    print instr
    
    elements = []
    elements.append(instr[0])
    instr = instr[1:]
    
    for element in instr:
        combo = elements[-1] + element
        #print combo, combo[::-1]
        if combo in combos:
            elements[-1] = combos[combo]
        elif combo[::-1] in combos:
            elements[-1] = combos[combo[::-1]]
        elif element in opposed:
            print "ahhh", elements, element, opposed[element]
            if opposed[element] in elements:
                elements = [""]
                print "EMPTY"
            else:
                elements.append(element)
        else:
            elements.append(element)
            
    elements = [item for item in elements if len(item) > 0]
    strElements = "["
    for element in elements:
        strElements = strElements + element + ", "
    strElements = strElements[:-2] + "]"
    if len(elements) == 0:
        strElements = '[]'
    
    
    output = "Case #" + str(i) + ": " + strElements + "\n"
    print output
    g.write(output)
    print ""
    
#5
#0 0 2 EA
#1 QRI 0 4 RRQR
#1 QFT 1 QF 7 FAQFDFQ
#1 EEZ 1 QE 7 QEEEERA
#0 1 QW 2 QW