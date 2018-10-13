import re
import sys

f = open('input.txt', 'r')

topper = f.readline()
top = topper.split()
L = int(top[0])
D = int(top[1])
N = int(top[2])

strl = []

for i in range(0,D):
    strl.append(f.readline())

def repl(strpar):
    return strpar.replace('(','[').replace(')',']')

regexps = []
for i in range(0,N):
    regexps.append(repl(f.readline()))
    
i = 1

strl = "".join(strl)

for regexp in regexps:
    print "Case #"+str(i)+": "+str(len(re.findall(regexp, strl)))
    i+=1