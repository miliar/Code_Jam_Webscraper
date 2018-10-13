#!/usr/bin/python

def flip(pancake, K):
    l = []
    for c in pancake:
        l.append(c)
    nflip = 0
    for i in range(0, len(pancake) - K + 1):
        if l[i] == '-':
            nflip += 1
            for j in range(0,K):
                if l[i +j] == '+':
                    l[i + j] = '-'
                else:
                    l[i + j] = '+'
    if '-' in l:
        return None
    else:
        return nflip

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0,t):
        s = raw_input()
        s = s.split()
        K = int(s[1])
        pancake = s[0]
        # print "pancake = ", pancake, "K = ", K 
        nflip = flip(pancake, K)
        if nflip == None:
            print "Case #" + str(i + 1) + ": IMPOSSIBLE"
        else:
            print "Case #" + str(i + 1) + ":", nflip
