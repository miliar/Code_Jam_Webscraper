import string

t = raw_input()
t = int(t)
testcases = 1
filein = open("map.txt",'r')

mapping = {}
def load():
    while 1 : 
        line = filein.readline()[:-1]
        if not line : 
            break
        words = string.split(line,' ')
        mapping[words[0]] = words[1]
        
def change(line):
    newline = ""
    for char in line : 
        if char == " " :
            newline = newline + char
        else :
            newline = newline +  mapping[char]
    return newline

load()
while t : 
    line = raw_input()
    print "Case #" + str(testcases) + ":" , 
    print change(line)
    t = t - 1
    testcases = testcases + 1
