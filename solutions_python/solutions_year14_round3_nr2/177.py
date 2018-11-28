import fileinput

def nextChar(word, index):
    ini_index = index
    for ind in range(index+1,len(word)):
        if word[ind] != word[ind-1]:
            return word[ind-1],ind-ini_index,ind
    return word[-1], len(word)-ini_index, len(word)

def resumeWord(word):
    vals = []
    quants = []
    val, quant, ind = nextChar(word,0)
    vals.append(val)
    quants.append(quant)
    while ind != len(word):
        val, quant,ind = nextChar(word,ind)
        vals.append(val)
        quants.append(quant)        
    return vals

def superResumeWord(word):
    word = resumeWord(word)
    ini = word[0] 
    end = word[-1]
    mid = []
    for i in range(1, len(word)-1):
        mid.append(word[i])
    return ini, end, mid, 1

def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)
        
def solve(wagons):     

    #wagons = "hhh hhhhhhhhnnnnnnnnnnnn iiyqtsskavvvppll hhhhhhhhhhhhhhh nnnnnnnnnnnn".split(" ")

    total_letters = set(''.join(wagons))
    resumes = [superResumeWord(wag) for wag in wagons]
    situation = {}
    
    for let in total_letters:
        situation[let] = [0,0,0,0]
    
    for res in resumes:
        if res[0] == res[1] and len(res[2]) == 0:
            situation[res[0]][3] += 1
        else:
            situation[res[0]][0]+=1
            situation[res[1]][1]+=1
            for i in range(len(res[2])):
                situation[res[2][i]][2] += 1    
    possible = True
    for key in situation:
        sit = situation[key]
        if (sit[0] - sit[1] != 0 and sit[2] != 0) or sit[0] > 1 or sit[1] > 1:
            possible = False
            break
    if possible:
        inis = 0
        ends = 0
        combs = 1

        for key in situation:
            situation[key][3] = factorial(situation[key][3])
            if situation[key][2] != 0:
                continue
            if situation[key][3] != 0 and (situation[key][0] == 0 and situation[key][1] == 0):
                inis += 1
                ends += 1
            elif situation[key][0] * situation[key][1] == 0:
                inis += situation[key][0]
                #ends += situation[key][1]
            combs *= max(situation[key][3],1)

        #resultat = factorial((inis+ends)/2)*combs
        resultat = factorial(inis)*combs

        #print str(inis)
        #print str(ends)
        #print str(combs)
        #print str(situation)

        
        return resultat
    return 0




fil = fileinput.input()
numcases = int(next(fil))

for case in range(1,numcases+1):
    wagons = int(next(fil))
    wagons = next(fil).replace("\n","").split(" ")
    print "Case #" + str(case)+": " + str(solve(wagons))

#solve("")         
