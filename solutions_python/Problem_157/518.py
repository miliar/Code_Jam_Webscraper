#!/usr/bin/python

import sys


def debug(msg):
#    return
    sys.stderr.write("\x1b[33;1m"+str(msg)+"\x1b[0m\n")

calc = {
    "11": "1",
    "1i": "i",
    "1j": "j",
    "1k": "k",
    "i1": "i",
    "ii": "-1",
    "ij": "k",
    "ik": "-j",
    "j1": "j",
    "ji": "-k",
    "jj": "-1",
    "jk": "i",
    "k1": "k",
    "ki": "j",
    "kj": "-i",
    "kk": "-1",

    "-11": "-1",
    "-1i": "-i",
    "-1j": "-j",
    "-1k": "-k",
    "-i1": "-i",
    "-ii": "1",
    "-ij": "-k",
    "-ik": "j",
    "-j1": "-j",
    "-ji": "k",
    "-jj": "1",
    "-jk": "-i",
    "-k1": "-k",
    "-ki": "-j",
    "-kj": "i",
    "-kk": "1",

    "1-1": "-1",
    "1-i": "-i",
    "1-j": "-j",
    "1-k": "-k",
    "i-1": "-i",
    "i-i": "1",
    "i-j": "-k",
    "i-k": "j",
    "j-1": "-j",
    "j-i": "k",
    "j-j": "1",
    "j-k": "-i",
    "k-1": "-k",
    "k-i": "-j",
    "k-j": "i",
    "k-k": "1",

    "-1-1": "1",
    "-1-i": "i",
    "-1-j": "j",
    "-1-k": "k",
    "-i-1": "i",
    "-i-i": "-1",
    "-i-j": "k",
    "-i-k": "-j",
    "-j-1": "j",
    "-j-i": "-k",
    "-j-j": "-1",
    "-j-k": "i",
    "-k-1": "k",
    "-k-i": "j",
    "-k-j": "-i",
    "-k-k": "-1",
}

def shrink(msg):
    total = "1"
#    debug(len(msg))
    for c in msg:
        total = calc[total + c]
    return total

def find(msg, letter, nb_max):
    nb = 0
    total = "1"
#    debug("looking for %s in (%d)%s" %(letter, len(msg), msg[:100]))
    for n, c in enumerate(msg):
        total = calc[total + c]

        if total == letter:
            nb += 1
            if nb >= nb_max:
#                print "found", letter, "in", msg[:n+1]
                return (n, msg[:n+1], msg[n+1:])

    return 0, "", msg

nb = int(raw_input())

ni_max = 30
nj_max = 30

for case in xrange(1, nb+1):
    l, x = [ int(i) for i in raw_input().split() ]

    val_short = raw_input()

    debug("case %d" % (case))
    # Strip all same value
    for i in val_short[1:]:
        if i != val_short[0]:
            break
    else:
        print "Case #%d: NO" % (case)
        continue

    val = val_short * x

    if l * x < 3:
        print "Case #%d: NO" % (case)
        continue

    resultat = "NO"
    soli = "Go"
    ni = 1
    while soli and ni < ni_max:
#        debug("ni: %4.2f%%" % (ni*100.0/ni_max))
        idx, soli, resi = find(val, "i", nb_max=ni)
        if soli:
            solj = "Go"
            nj = 1
            while solj and nj < nj_max:
                idx, solj, resj  = find(resi, "j", nb_max=nj)

                if solj:
                    solk = "Go"
                    nk = 1
                    while solk and nk < 2:
                        idx, solk, resk  = find(resj, "k", nb_max=nk)
                        if solk and shrink(resk) == "1":
                            debug("%s   %s   %s" % (soli, solj, solk))
                            resultat = "YES"
                            soli = ""
                            solj = ""
                            solk = ""
                            continue

                        nk += 1

                nj += 1

        ni += 1

    print "Case #%d: %s" % (case, resultat)
