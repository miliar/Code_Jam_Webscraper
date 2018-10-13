
def computeNValue(name, n):
    nValue = 0
    for start in range(len(name) - n + 1):
        end = start + n
        while end < len(name) + 1:
            if (hasNConsonant(name[start:end], n)):
                nValue += len(name) + 1 - end
                #print("start:",start,",end:",end,",nval:",nValue)
                break
            end += 1
    return nValue

def hasNConsonant(name, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(name) - n + 1):
        noVowel = True
        for c in name[i:i+n+1]:
            if c in vowels:
                noVowel = False
                break
        if noVowel:
            return True
    return False

#print(computeNValue('quartz', 3))
#print(computeNValue('straight', 3))
#print(computeNValue('gcj', 2))
#print(computeNValue('tsetse', 2))

import sys

outputs = []
with open(sys.argv[1], 'r') as fin:
    inputCount = int(next(fin))
    while 0 < inputCount:
        indata = next(fin).split()
        outputs.append(computeNValue(indata[0], int(indata[1])))
        inputCount -= 1

fout = open(sys.argv[2], 'wt')
for i, output in enumerate(outputs):
    fout.write('Case #' + str(i + 1) + ': ' + str(output) + "\n")
fout.close()

