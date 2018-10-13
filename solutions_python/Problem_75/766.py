import re

i = open('B-small-attempt1.in', 'r')

T = int(i.readline())

cases = []
for q in range(T):
    cases.append(i.readline()) 
i.close()

casenum = 1
o = open('B-small-attempt1.out', 'w')
for case in cases:
    segs = re.split('[0-9]+', case)
    combs = re.sub('\W+', '', segs[1])
    opps = re.sub('\W+', '', segs[2])
    input = re.sub('\W+', '', segs[3])
    
    combs = re.split('\W+', combs)
    opps = re.split('\W+', opps)
    
    output = []
    for char in input:
        output.append(char)
        if len(output) > 1:
            comb1 = output[len(output) - 1]
            comb2 = output[len(output) - 2]
            pos1, pos2 = comb1+comb2, comb2+comb1
            combfound = False
            for comb in combs:
                if (pos1 == comb[:2]) or (pos2 ==comb[:2]):
                    output = output[:len(output)-2]
                    output.append(comb[2])
                    combFound = True
                    break
            if not combfound:
                opp1 = output[len(output)-1]
                for char in output:
                    pos1, pos2 = opp1+char, char+opp1
                    if (pos1 in opps) or (pos2 in opps):
                        output = []
                        break
    result = str('Case #'+str(casenum)+': '+str(output)+'\n')
    result = result.replace("'", '')
    o.write(result)
    casenum += 1
    
o.close()