import sys, os

infile = open('A-small-attempt0.in', 'r')
output = open('tongues.out', 'w')

inputs = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
         'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
         'de kr kd eoya kw aej tysr re ujdr lkgc jv',
         'q',
         'e',
         'y',
         'z']
outputs = ['our language is impossible to understand',
          'there are twenty six factorial possibilities',
          'so it is okay if you want to just give up',
          'z',
          'o',
          'a',
          'q']

mydict = {}

for i in range(0, len(inputs)):
    in1 = inputs[i]
    in2 = outputs[i]
    for j in range(0, len(in1)):
        charOut = in1[j]
        charIn = in2[j]
        mydict[charOut] = charIn
        
def decode(inStr):
    outStr = ""
    for char in inStr:
        outStr += mydict[char]
    return outStr

def doProblem(num, inStr):
    println("Case #" + str(num) + ": " + decode(inStr))

def println(line):
    print line
    output.write(line + "\n")
    


lines = infile.readlines()
cases = int(lines[0])
for i in range(0, cases):
    doProblem(i+1, lines[i+1].strip())

infile.close()
output.close()
