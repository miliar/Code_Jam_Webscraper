'''
Created on May 6, 2011

@author: gyftdresaw
'''

from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

for i in xrange(trials):
    nums = int(infile.readline())
    vals = [int(x) for x in split(infile.readline())]
    
    tmp = vals[0]
    index = 1
    while index < len(vals):
        tmp = tmp^vals[index]
        index += 1
    if tmp == 0:
        best = sum(vals) - min(vals)
        s = "Case #%d: %d\n" %((i+1),best)
    else:
        s = "Case #%d: NO\n" % (i+1)
        
    outfile.write(s)
    print s

infile.close()
outfile.close()
    