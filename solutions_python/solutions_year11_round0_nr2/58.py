'''
Created on May 6, 2011

@author: gyftdresaw
'''

from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

for i in xrange(trials):
    cmatrix = [[-1 for x in xrange(26)] for y in xrange(26)]
    dmatrix = [[False for x in xrange(26)] for y in xrange(26)]
    vals = split(infile.readline())
    for j in xrange(int(vals[0])):
        config = vals[1+j]
        cmatrix[ord(config[0]) - ord('A')][ord(config[1]) - ord('A')] = ord(config[2]) - ord('A')
        cmatrix[ord(config[1]) - ord('A')][ord(config[0]) - ord('A')] = ord(config[2]) - ord('A')
    for j in xrange(int(vals[1+int(vals[0])])):
        config = vals[2+int(vals[0])+j]
        dmatrix[ord(config[0]) - ord('A')][ord(config[1]) - ord('A')] = True
        dmatrix[ord(config[1]) - ord('A')][ord(config[0]) - ord('A')] = True\
    
    inv = vals[-1]
    endlst = []
    for j in xrange(len(inv)):
        if len(endlst) == 0:
            endlst.append(inv[j])
        else:
            new = cmatrix[ord(inv[j]) - ord('A')][ord(endlst[-1])-ord('A')]
            if new != -1:
                endlst.pop()
                endlst.append(chr(new + ord('A')))
            else:
                test = False
                for c in endlst:
                    test = test or dmatrix[ord(inv[j]) - ord('A')][ord(c) - ord('A')]
                if test:
                    endlst = []
                else:
                    endlst.append(inv[j])
    s = "Case #%d: [" % (i+1)
    for c in xrange(len(endlst)):
        if c < len(endlst) - 1:
            s += endlst[c] + ", "
        else:
            s += endlst[c]
    s += "]\n"
    
    outfile.write(s)
    print s
    
    
    
    
    
    

infile.close()
outfile.close()