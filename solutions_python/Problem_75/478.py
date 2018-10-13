#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     08/05/2011
# Copyright:   (c) wani 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

def hands(d_combs,d_vanish,draws):
    hand = []
    vanish = set([])
    vanish_old = set([])
    for card in draws:
        if len(hand) > 0:
            if (hand[-1],card) in d_combs:
                last = hand.pop()
                hand.append(d_combs[(last,card)])
                if last in d_vanish:
                    vanish = vanish_old
            elif card in vanish:
                hand = []
                vanish.clear()
                vanish_old.clear()
            elif card in d_vanish:
                hand.append(card)
                vanish_old = copy.copy(vanish)
                vanish |= set(d_vanish[card])
            else:
                hand.append(card)
        else:
            if card in d_vanish:
                hand.append(card)
                vanish_old = copy.copy(vanish)
                vanish |= set(d_vanish[card])
            else:
                hand.append(card)
    return hand

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        l = f.readline().strip().split()
        c = int(l.pop(0))
        d_combs = {}
        d_vanish = {}
        for n in range(c):
            s = l.pop(0)
            d_combs[(s[0],s[1])] = s[2]
            d_combs[(s[1],s[0])] = s[2]
        d = int(l.pop(0))
        for n in range(d):
            s = l.pop(0)
            if s[0] in d_vanish:
                d_vanish[s[0]] = d_vanish[s[0]] + [s[1]]
            else:
                d_vanish[s[0]] = [s[1]]
            if s[1] in d_vanish:
                d_vanish[s[1]] = d_vanish[s[1]] + [s[0]]
            else:
                d_vanish[s[1]] = [s[0]]
        draws = l.pop(1)
#        print (d_combs,d_vanish,draws)
        out = "Case #%d: [%s]"%(i+1,", ".join(hands(d_combs,d_vanish,draws))) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
