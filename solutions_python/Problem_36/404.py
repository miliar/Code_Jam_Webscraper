#!/usr/bin/env python
"""google code jam : welcome to google code jam"""


import sys

class counterClass :
    def __init__(self) :
        self.i = 0
    def inc(self):
        self.i = self.i + 1

def analyse_text(txt,phaseToFind = "welcome to code jam") :
    print('finding occurences of "%s" in "%s"' %(phaseToFind,txt))
    #building forwarding maps
    fM = []
    def findall(c,i):
        r = []
        i = txt.find(c,i)
        while i <> - 1 :
            r.append(i)
            i = txt.find(c,i+1)
        return r
    for c in phaseToFind :
        fM.append([findall(c,i) for i in range(len(txt))]) #very inefficent, but quick to code.
        
    #fMap
    #for c,f in zip(phaseToFind,fM) :
    #    print(c,f)
    
    count = counterClass()
    pMax = len(phaseToFind)-1
    def walkTree(p,i): #p char location in phraseToFind, i in location in txt
        #print(p,i,fM[p][i])
        for opt in fM[p][i] :
            if p < pMax :
                walkTree(p+1, opt) #this should be safe proved phaseTofind does not have two consecutive identical chars
            else :
                count.inc()
    walkTree(0,0)
    return count.i

def last4digits(i) :
    s = str(i)
    while len(s) < 4 :
        s = '0' + s
    return s[len(s)-4:len(s)]

def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    N = int(lines[0].strip())
    print('file "%s" contains %i texts' % (datafile,N))
    texts = [ ln.strip() for ln in lines[1:N+1]]

    output = []
    for txt,i in zip(texts,range(N)) :
        res = analyse_text(txt)
        outText = 'Case #%i: %s' %(i+1,last4digits(res))
        #outText = outText + '\n'.join([' '.join(row) for row in res])
        print(outText)
        output.append(outText)

    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()

#print(last4digits(123456))
