#!/usr/bin/python

G = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
     "de kr kd eoya kw aej tysr re ujdr lkgc jv"
     ]

S = ["our language is impossible to understand",
     "there are twenty six factorial possibilities",
     "so it is okay if you want to just give up"
     ]

if __name__ == "__main__":
    d = dict()
    for i in xrange(3):
        g = G[i]
        s = S[i]
        for j in xrange(len(g)):
            d[g[j]] = s[j]

    d['z'] = 'q'
    d['q'] = 'z'

    # Till this point we have made the mapping dictionary
    T = int(raw_input())  # T is the number of Test Cases
    for i in xrange(T):
        gin = raw_input()  # googlerese input string
        sout = ""
        for j in xrange(len(gin)):
            sout += d[gin[j]]
        print "Case #" + str(i+1) + ": " + sout
