fr = open("input.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
    global curLine
    global lines
    curLine += 1
    return lines[curLine-1]
    
def flip(c):
    if c == '-':
        return '+'
        
    return '-'

while curTest < numTests:
    pancakes, k = getLine().strip().split()
    k = int(k)
    pancakes = list(pancakes)
    
    numPancakes = len(pancakes)
    i = 0
    
    numFlips = 0
    
    while i <= (numPancakes - k):
        if pancakes[i] == '-':
            if (i+k) <= numPancakes:
                for n in range(i, i+k):
                    pancakes[n] = flip(pancakes[n])
                numFlips += 1
        i += 1
                
    good = True
    for p in pancakes:
        if p == '-':
            good = False
            break
            
    if good:
        fw.write("Case #%d: %s\n" % (curTest+1, numFlips))
    else:
        fw.write("Case #%d: IMPOSSIBLE\n" % (curTest+1))

    curTest += 1
                    
fr.close()
fw.close()