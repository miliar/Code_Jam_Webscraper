
def combine(comb, spell, top):
    key = tuple(sorted((spell, top)))
    result = comb.get(key, None)
    return result

def processcase(comb, opp, spells_input):
    
    elist = []
    for spell in spells_input:
        if not elist:
            elist.append(spell)
            continue
        top = elist[-1]
        combine_result = combine(comb, spell, top)
        if not combine_result: #no combino, a mirar si es opposed
            for s in elist:
                if spell in opp.get(s, []):
                    elist = []
                    break
            else:
                elist.append(spell)
        else: #si si combino
            elist.pop()
            elist.append(combine_result)
                        
    return elist

f = open("in")

testcases = int(f.readline())

for case in range(testcases):
    line = f.readline()
    linesplit = line.split()
    combines = int(linesplit[0])
    comb = {}
    opp = {}
    
    idx = 1
    for i in range(1, combines+1):
        combstr = linesplit[i]
        key = sorted((combstr[0], combstr[1]))
        comb[tuple(key)] = combstr[2]
        idx += 1
        
    opposseds = int(linesplit[idx])
    idxold = idx
    for i in range(1, opposseds+1):
        oppstr = linesplit[i+idxold]

        if not opp.get(oppstr[0], []):
            opp[oppstr[0]] = set([oppstr[1]])
        else:
            opp[oppstr[0]].add(oppstr[1])
            
        if not opp.get(oppstr[1], []):
            opp[oppstr[1]] = set([oppstr[0]])
        else:
            opp[oppstr[1]].add(oppstr[0])

        idx += 1
    
    idx += 1
    nspells = int(linesplit[idx])
    idx += 1
    spells_input = linesplit[idx]
    
    #print(comb, opp, spells_input)
    solution = processcase(comb, opp, spells_input)
    
    print("Case #{}: {}\n".format(case+1, "["+", ".join([i for i in solution])+"]"), end="")

f.close()
