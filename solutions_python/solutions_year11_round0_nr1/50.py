'''
Created on May 6, 2011

@author: gyftdresaw
'''

from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

for i in xrange(trials):
    vals = split(infile.readline())
    tlst = []
    indivlst = [[1] for x in xrange(2)]
    for j in xrange(int(vals[0])):
        if vals[1+2*j] == 'O':
            tlst.append(0)
            indivlst[0].append(int(vals[2+2*j]))
        else:
            tlst.append(1)
            indivlst[1].append(int(vals[2+2*j]))
    
    time = 0
    last = tlst[0]
    index = [1,1]
    total = 0
    for y in tlst:
        nexttime = abs(indivlst[y][index[y]] - indivlst[y][index[y]-1])
        #print (time,nexttime,index,total)
        if last == y:
            total += nexttime + 1
            time += nexttime + 1
        else:
            if nexttime <= time:
                total += 1
                time = 1
            else:
                total += nexttime - time + 1
                time = nexttime - time + 1
        index[y] += 1
        last = y
        
    #print (time,nexttime,index,total)
    s = "Case #%d: %d\n" % ((i+1),total)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()