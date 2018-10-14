import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

def wordlength(word):
    #print word
    length = 0
    for w in word:
        print w
        if w[0] == "(":
            length += 1
        else:
            length += len(w)
            
    return length
    
def getpossiblewords(current, rest, depth, length, answers):
    if depth == length or depth == len(rest):
        answers.append(current)
    else:
        if rest[depth][0] == "(":
            for i in range(1, len(rest[depth])):
                #print (str(rest) + " :: " + str(depth) + " :: " + str(i))
                getpossiblewords(current + rest[depth][i], rest, depth + 1, length, answers)
        else:
            getpossiblewords(current + rest[depth], rest, depth + 1, length, answers)
    
    pass 

f = open(sys.argv[1], 'r')

start=1
word = 0
set = 0
words = []
probset = []
L = 0
D = 0
N = 0
beginwords = 0
beginprobset = 0

readdata = []

for data in f:
    readdata.append(data.strip())
        
f.close()


init = readdata[0].split(" ")
L = int(init[0])
D = int(init[1])
N = int(init[2])

words = readdata[1:D+1]
sets = readdata[D+1:D+1+N]

#print words
#print sets

counter = 1

for s in sets:
    currword = ""
    letters = []
    insub = False
    for l in s:
        if insub and l != ")":
            currword += l
        elif l == "(":
            insub = True
        elif l != "(" and not insub:
            letters.append(l)
        elif l == ")":
            letters.append(currword)
            insub = False
            currword = ""
            
    if len(letters) != L:
        print "Case #" + str(counter) + ": 0"
    else:
        possible = 0
        #print "\n\n" + str(letters)
        for w in words:
            #print w
            init = True
            for i in range (0, L):
                if w[i] not in letters[i]:
                    init = False
            if init:
                possible += 1
        print "Case #" + str(counter) + ": " + str(possible)
            
        
    counter += 1
            
