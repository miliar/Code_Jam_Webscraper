
import psyco, sys
psyco.full()

# http://myphotoblogbeta.blogspot.com/2007/07/python-convert-to-and-from-base-b.html
def tobase(base,number):
    global tb
    def tb(b,n,result=''):
        if n == 0: return result
        else: return tb(b,n/b,str(n%b)+result)

    if type(base) != type(1):
        raise TypeError, 'invalid base for tobase()'
    if base <= 0:
        raise ValueError, 'invalid base for tobase(): %s' % base
    if type(number) != type(1) and type(number) != type(1L):
        raise TypeError, 'tobase() of non-integer'
    if number == 0:
        return '0'
    if number > 0:
        return tb(base, number)
    if number < 0:
        return '-' + tb(base, -1*number)


unhappies = set() # items are: (base,sn) 
happies = set() # (base,sn) items

def happy(n, base):
    global unhappies, happies
    sn = tobase(base,n)
    perhapsUnhappies = set()
    while not (base,sn) in unhappies and not (base,sn) in perhapsUnhappies:
        #print base,sn,perhapsUnhappies,len(unhappies)
        
        if (base,sn) in happies:
            return True
        
        perhapsUnhappies.add((base,sn))
        summed = 0
        for c in sn:
            summed += int(c) * int(c)
        sn = tobase(base,summed)
        if summed == 1:
            happies.update(perhapsUnhappies)
            #print len(happies), len(unhappies)
            return True
    unhappies.update(perhapsUnhappies)
    return False

def gen_happy(base):
    n = 2
    while True:
        if happy(n,base):
            yield n
        n += 1

def calc2(basesStr):
    smallest = None
    cnt = 0
    tgtCnt = len(basesStr)
    hgens = {} 
    prog = []
    for bs in basesStr:
        b = int(bs)
        hgens[b] = gen_happy(b)
        prog.append([b, 1])
        
    def minKey(a):
        return a[1]
    
    i = 0
    while True:
        minb = min(prog, key=minKey)
        nex = hgens[minb[0]].next()
        minb[1] = nex
        
        #i += 1
        #if i % 100 == 0:
        #    print prog
        
        #print nex, minb, prog
        
        a = minb[1]
        allEquals = True
        for bb in prog:
             if bb[1] != a:
                 allEquals = False
                 break
        if allEquals:
            return a


# TESTING
#n = 2
#while True:
#    if happy(n, 7):
#        print n
#    n += 1    


def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    print "Case #%d: %d" % (cn, calc2(line.split(' ')))
    cn += 1
