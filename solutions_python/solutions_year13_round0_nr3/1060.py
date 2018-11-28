
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

fairsquares = [1,4,9,121,484]

for i in xrange(trials):
    limits = [int(x) for x in infile.readline().split()]
    
    result = sum([x >= limits[0] and x <= limits[1] for x in fairsquares])
    
    s = "Case #%d: %d\n" % (i+1,result)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()