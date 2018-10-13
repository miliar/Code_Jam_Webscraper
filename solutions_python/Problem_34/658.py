import os
import math

os.chdir(os.getcwd())
caseLine = ""
fin = open("A-large.in", "r")
lines = fin.readlines();

fin.close()
first = lines[0].split(' ')

numLetters = first[0]
numWords = first[1]
numCases = first[2]

words = []
cases = []
for i in range(1, int(numWords) +1):

    words.append(lines[i])

for j in range(int(numWords) + 1, len(lines)):
    
    possible = []
    count = 0
    for k in range(0, int(numLetters)):
        let = []
        
        if (lines[j][count] == '('):
            count += 1
            while lines[j][count] != ')':
                
                let.append(lines[j][count])
                count += 1
            count += 1

        else:
            
            let.append(lines[j][count])
            count += 1
        possible.append(let)

    poss = 0
    isOk = 0
    posslist = []
    for k in range(0, len(words)):
        isOk = 0
        
        for l in range(len(possible)):
            isOk = 0
            
            for m in range(0, len(possible[l])):
                if words[k][l] == possible[l][m]:
                    
                    isOk = 1
                    break
            if isOk != 1:
                break
        if isOk == 1:
            poss += 1
        
            
    caseLine = caseLine + "Case #" + str(j-int(numWords)) + ": " + str(poss) + "\n"
                
fout = open("outlarge.txt", "w")
fout.write(caseLine)
fout.close()
        

        
        
                
                
                
            
        
        
        


