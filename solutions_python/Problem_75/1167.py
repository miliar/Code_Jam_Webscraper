import sys

def main(args):
    input = open(args[0])
    cases = int(input.readline())
    for i in range(cases):
        casenum = i + 1
        casein = input.readline().split(" ")
        index = 0
        combinations = {}
        oppositions = {}
        combos = int(casein[index])
        index += 1
        for x in range(combos):
            comb = [casein[index][0], casein[index][1]]
            comb.sort()
            combinations[tuple(comb)] = casein[index][2]
            index += 1
            
        oppos = int(casein[index])
        index += 1
        for x in range(oppos):
            if(not oppositions.has_key(casein[index][0])):
                oppositions[casein[index][0]] = []
            oppositions[casein[index][0]].append(casein[index][1])
            if(not oppositions.has_key(casein[index][1])):
                oppositions[casein[index][1]] = []
            oppositions[casein[index][1]].append(casein[index][0])
            index += 1
            
        index += 1
        #now, index points to the input string
        #each char
        result = [];
        prev = None
        invokations = casein[index].strip()
        for c in invokations:
            if(prev):
                comb = [c, prev]
                comb.sort()
                if(combinations.has_key(tuple(comb))):
                    result = result[0:-1]
                    result.append(combinations[tuple(comb)])
                    prev = result[-1]
                    continue
                elif(oppositions.has_key(c)):
                    cleared = False;
                    for o in oppositions[c]:
                        if(result.count(o) > 0):
                            result = []
                            prev = None
                            cleared = True
                            break
                    if(cleared):
                        continue
            
            result.append(c)
            prev = c
        
        print "Case #{0}: [{1}]".format(casenum, ", ".join(result))
        #print combinations
        #print oppositions
        

if __name__ == '__main__':
    main(sys.argv[1:])