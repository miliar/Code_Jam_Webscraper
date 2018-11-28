import sys

# Check wether the word is a possible candidate. Returns a 1 if it is
def possibility(pattern, word):
    for i in range(0,len(word)):
        if pattern[i].find(word[i]) == -1:
            return 0
    return 1

# Generates a list pattern for easier pattern checking
def generatePatterns(pattern):
    patternChar = []
    i = 0
    pattern = pattern.rstrip('\n')
    while(i !=  len(pattern)):
        if(pattern[i] == "("):
            charPattern = ""
            i += 1
            while(pattern[i] != ")"):
                charPattern += pattern[i]
                i += 1
            i += 1
            patternChar.append(charPattern)
        else:
            patternChar.append(pattern[i])
            i += 1
    return patternChar

# Toplevel. Takes in attributes, then finds number of possibilities and returns
# as array
def interpret(L, D, N, dict, patterns):
    possibilities = []
    for line in patterns:
        pattern = generatePatterns(line)
        number = 0
        for word in dict:
            number += possibility(pattern, word.rstrip("").rstrip("\n"))
        possibilities.append(number)
    return possibilities
        
# The actual code that's executed
fh = open(sys.argv[1], "r")
output = open("outputAlien.txt", "w")
lines = fh.readlines()
L,D,N = lines[0].split()
possibilities = interpret(L, D, N, lines[1:int(D) + 1], lines[int(D) + 1:int(D) + int(N) + 1])
i = 1
for count in possibilities:
    output.write("Case #" + str(i) + ": " + str(count) + "\n")
    i += 1

output.close()
