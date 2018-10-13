#!/usr/bin/python

def val(s, b, hash):
    acc = 0
    for c in s:
        acc *= b
        acc += hash[c]
    return acc

def minval(s):

    digs = []
    dset = set([])
    dhash = {}

    for c in s:
        if not c in dset:
            digs.append(c)
        dset.add(c)

    if len(dset) == 1:
        dhash[digs[0]] = 1
        return val(s, 2, dhash)

    dhash[digs[0]] = 1

    if digs[1:]:
        dhash[digs[1]] = 0

    for i, dig in enumerate(digs[2:]):
        dhash[dig] = i + 2

    return val(s, len(dset), dhash)

if __name__ == "__main__":
    n = int(raw_input())

    for i in xrange(n):
        #s = raw_input()
        #print s
        print "Case #%d: %d" % (i + 1, minval(raw_input()))
