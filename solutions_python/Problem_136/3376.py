'''
Created on 12-apr.-2014

@author: Joachim
'''

group = "small"

infile =  open("B-%s.txt" % group, "r")
out = open("B-%s_out.txt" % group, "w")

total_cases = int(infile.readline())

for i in xrange(1, total_cases+1):
    line = infile.readline()
    c, f, x = [float(x) for x in line.split(" ")]
    
    prev = x/2.0
    farms=0
    time = prev
    while time <= prev:
        prev = time
        farms += 1
        time = 0
        for j in xrange(farms):
            time += c/(2.0+j*f)
        time += x/(2.0+farms*f)
    out.write("Case #%d: %.7f\n" % (i, prev))
    

out.close()
infile.close()