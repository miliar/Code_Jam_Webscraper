import string

def getline(f):
    return string.split(f.readline(), "\n")[0]
    
    
infile = open("A-large.in",'r')

numCases = int(getline(infile))

for case in xrange(numCases):
    length = getline(infile)
    vec1 = string.split(getline(infile))
    vec2 = string.split(getline(infile))
    
    for i in xrange(len(vec1)):
        vec1[i] = int(vec1[i])
        vec2[i] = int(vec2[i])
        
    vec1.sort()
    vec2.sort()
    
    sum = 0
    while vec1:
        sum += vec1.pop() * vec2.pop(0)
        
    print "Case #%d: %d" % (case + 1, sum)