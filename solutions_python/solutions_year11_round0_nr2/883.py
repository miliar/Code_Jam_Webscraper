import sys
import re

#helper
def nonepop(l):
    if len(l) == 0:
        return None
    else:
        return l.pop()
#end helper

write = 'write' in sys.argv
filein = sys.argv[1]
fileout = re.sub('\.in','',filein) + ".out"
fin = open(filein,'r')
if write: fout = open(fileout,'w')
    
n = int(fin.readline())

for i in range(1,n+1):
    l = fin.readline()[0:-1].split(" ")
    l.reverse()
    ### start
    nrep = int(l.pop())
    reps = list()
    for j in range(0,nrep):
        rep = l.pop()
        reps.append((rep[:2],rep[2]))
    
    nopp = int(l.pop())
    opps = list()
    for j in range(0,nopp):
        opps.append(l.pop())
    
    l.pop()
    invs = list(l.pop())
    if not write: print reps,opps,invs
    invs.reverse()
    out = list()
    while len(invs) > 0:
        inv = invs.pop()
        out.append(inv)
        if not write: print out
        #check replacements
        if len(out)>=2:
            l2 = out[-2:]
            repl = False
            for rep in reps:
                if (l2[0] == rep[0][0] and l2[1] in rep[0][1]) or (l2[0] == rep[0][1] and l2[1] in rep[0][0]):
                    #replace
                    out.pop(),out.pop()
                    out.append(rep[1])
                    if not write: print 'replace ' + str(l2) + ' by ' + rep[1] + ' -> ' + str(out)
                    repl = True

            if not repl:
                #check opposing
                for char in out[:-1]:
                    for opp in opps:
                        if (inv == opp[0] and char == opp[1]) or (inv == opp[1] and char == opp[0]):
                            #replace
                            out = list()
                            if not write: print 'reset list (%s %s)' % (inv,char)
    
    if not write: print '==================='
    sol = "Case #%i: %s\n" % (i,"[" + ", ".join(out) + "]")
    print sol
    if write: fout.write(sol)

if write: fout.close()