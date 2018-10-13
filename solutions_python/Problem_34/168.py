import sys
import re

inp = open(sys.argv[1])
lines = inp.readlines()
inp.close()

L = int(lines[0].split(' ')[0])
D = int(lines[0].split(' ')[1])
N = int(lines[0].split(' ')[2])

words = []

for i in range(0,D):
    words += [lines[1+i]]

for i in range(0,N):
    pattern = lines[1+D+i].replace("(", "[").replace(")","]")

    ret = 0
    for word in words:
        if re.match(pattern, word): ret+=1

    print "Case #%d: %d" % ((i+1), ret)

    
    

