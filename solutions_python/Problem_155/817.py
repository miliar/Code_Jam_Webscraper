
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

def people_needed(smax,scounts):
    current_people = 0
    needed = 0
    for i in xrange(len(scounts)):
        if current_people < i and scounts[i] > 0:
            n = i - current_people
            current_people += n
            needed += n
        current_people += scounts[i]
    return needed

for i in xrange(trials):

    params = infile.readline().split()
    smax = int(params[0])
    scounts = [int(d) for d in params[1]]

    print smax,scounts

    s = "Case #%d: %d\n" % (i+1,people_needed(smax,scounts))
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
