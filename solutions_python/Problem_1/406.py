#aa = search engines
#bb = queues
from string import *

inn = open('input.txt', 'r')
def getz():
    global inn
    return inn.readline().strip()

def problem1(bb,aa,n):
    print "%s%d%s%d" % ("Case #", n, ": ", search(bb,list(aa),list(aa)))
def search(bb,aa,master):
    #print bb,aa,master
    if len(aa) == 0: return 1+search(bb,list(master),list(master))
    if len(bb) == 0: return 0
    if bb[0] in aa:
        aa.remove(bb[0])
        if len(aa) == 0:
            z = list(master)
            z.remove(bb[0])
            return 1+search(bb[1:], list(z), list(master))
    return search(bb[1:],list(aa),list(master))

n = int(getz())
for testcase in range(n):
    m = int(getz())
    aa = []
    bb = []
    for i in range(m):
        aa.append(getz())
    m2 = int(getz())
    for i in range(m2):
        bb.append(getz())
    #print bb,aa
    problem1(bb,aa,1+testcase)
    
