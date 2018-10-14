#!/usr/bin/python2.5
def main():
    for case in range(input()):
        nse = input()
        se = []
        for i in range(nse):
            se.append(raw_input())
        nq = input()
        qs = []
        for j in range(nq):
            qs.append(raw_input())
        
#        ts = uniq(qs)
#        if len(ts)<len(se):
#            print 'Case #%s: %s' % (case+1, 0)
#            return
#
        tse = list(se)
        if len(qs) > 1:tse.remove(qs[0])
        ns = 0
        for k in range(1, len(qs)):
            if qs[k] == qs[k-1]:
                continue;
            else: 
                if tse.count(qs[k]) > 0:
                    tse.remove(qs[k])
                    if len(tse) == 0:
                        tse = list(se)
                        tse.remove(qs[k])
                        ns = ns + 1
        
        print 'Case #%s: %s' % (case+1, ns)
#           
#def uniq(alist):
#    set = {}
#    map(set.__setitem__, alist, [])
#    return set.keys()
#
main()
