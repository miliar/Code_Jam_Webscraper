#!/usr/bin/python2.5
def main():
    for case in range(input()):
        ta = input()
        na, nb=map(int, raw_input().split())
        timea = [ raw_input().split() for i in range(na)]
        timeb = [ raw_input().split() for i in range(nb)]
        for i in range(na):
            timea[i]=map(tom, timea[i])
        for i in range(nb):
            timeb[i]=map(tom, timeb[i])
        timea.sort()
        timeb.sort()
        
        nta=ntb=0
        while len(timea) > 0 and len(timeb) > 0:
            aside = timea[0] < timeb[0]
            if aside: 
                train=timea[0]       
                nta=nta+1
            else: 
                train=timeb[0]
                ntb=ntb+1
            ct=train[0]
            while(ct<=train[0]):
                if aside:
                    ct=train[1]+ta
                    timea.remove(train)
                    aside=False
                    for i in range(len(timeb)):
                        if timeb[i][0]>= ct:
                            train=timeb[i]
			    break
                else:
                    ct=train[1]+ta
                    timeb.remove(train)
                    aside=True
                    for i in range(len(timea)):
                        if timea[i][0]>=ct:
                            train=timea[i]
			    break
            
        nta += len(timea)
        ntb += len(timeb)
        print 'Case #%s: %s %s' % (case + 1, nta, ntb)

def tom(hm):
    h, m = map(int, hm.split(':'))
    return h*60+m
main()
