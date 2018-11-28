import sys
import re

#helper
def nonepop(l):
    if len(l) == 0:
        return None
    else:
        return l.pop()
#end helper


filein = sys.argv[1]
fileout = re.sub('\.in','',filein) + ".out"
fin = open(filein,'r')
fout = open(fileout,'w')
### start

n = int(fin.readline())

for i in range(1,n+1):
    l = fin.readline()[0:-1]
    #print l
    els = l.split(" ")
    els.reverse()
    c = int(els.pop())
    
    
    bb,bo,cs = list(), list(), list()
    
    for j in range(0,c):
        col = els.pop()
        if col == 'O':
            cs.insert(0,'O')
            bo.insert(0,int(els.pop()))
        else:
            cs.insert(0,'B')
            bb.insert(0,int(els.pop()))
    
    #print cs,bo,bb
    timer = 0
    b,o = 1,1
    #start simulation
    next_c = nonepop(cs)
    next_o = nonepop(bo)
    next_b = nonepop(bb)
    
    while next_c:
        timer+=1
        o_clicked, b_clicked = False,False
        #print next_c,o,next_o
        if next_c == 'O' and next_o == o:
            next_c = nonepop(cs)
            next_o = nonepop(bo)
            o_clicked = True
        elif next_c == 'B' and next_b == b: 
            next_c = nonepop(cs)
            next_b = nonepop(bb)
            b_clicked = True
        
        if not o_clicked:
            #move o towards next 
            if next_o:
                if next_o>o:
                    o+=1
                elif next_o<o:
                    o-=1
        if not b_clicked:
            #move o towards next 
            if next_b:
                if next_b>b:
                    b+=1
                elif next_b<b:
                    b-=1

    fout.write("Case #%i: %i\n" % (i,timer))

fout.close()