#!/usr/bin/env python

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
	res = []
	for i in xrange(N):
		res.append(foo())
	return res
def readlinearray(foo): return map(foo, raw_input().split())

def playWar(N, naomi, ken):

    for i in xrange(N):
        for j in xrange(len(ken)):
            if(naomi[i] < ken[j]):
                ken.remove(ken[j])
                break;


    return len(ken)

def playDeceitfulWar(N, naomi, ken):

# remove max
    while True:
        if len(naomi) <= 1:
            break
        if max(naomi, key=float) >  max(ken, key=float):
            break

        ken.pop()
        naomi.pop(0)

    win = 0
# start deceive ken
    for i in ken:
        if(len(naomi) == 1):
            if i < naomi[0]:
                win += 1
                break
            #just compare
        for j in naomi:
            if i < j :
                win += 1
                naomi.remove(j)
                break;

    return win


testCount = eval(raw_input())

for test in xrange(1, testCount+1):

    Blocks = eval(raw_input())

    NaomiBls = sorted(map(float, raw_input().split()), key=float)
    KenBls = sorted(map(float, raw_input().split()), key=float)

    NaomiBls1 = list(NaomiBls)
    KenBls1 = list(KenBls)

    #print playDeceitfulWar(Blocks, NaomiBls, KenBls)
    #print playWar(Blocks, NaomiBls1, KenBls1)

    print "Case #%d: %d %d" % (test,playDeceitfulWar(Blocks, NaomiBls, KenBls),playWar(Blocks, NaomiBls1, KenBls1))



