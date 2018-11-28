#Paul Johnson
#GCJ 2012 Problem A

from sys import *

#First, create the mapping from the information provided
code = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
eng = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

map = {'y':'a','e':'o', 'q':'z', 'z':'q'}

for x in range(len(code)):
    if code[x] not in map.keys():
        map[code[x]] = eng[x]
    else:
        if map[code[x]] != eng[x]: print "scream"
print len(map.keys())

#Check the map for the appropriate number of keys and the presence of every letter
m = map.keys()
m.sort()
print m
l = []
for x in m: l.append(map[x])
l.sort()
print l

#Translate!

input = open(argv[1],'r')
output = open(argv[2],'w')

lines = int(input.readline())

for x in range(lines):
    inp = input.readline()
    out = ''
    for y in inp:
        if y != "\n":out+=map[y]
    output.write("Case #%i: %s\n"%(x+1,out))


input.close()
output.close()