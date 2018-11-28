#!/usr/bin/python
import sys, os

def usage():
    print("%s " % sys.argv[0] )

def transform(combine, query):
    return query

def rev(combine, query):
    return query

def translate(comb_dict, rev_dict, query):
    ret = []
    for char in query:
        i = char
        ret.append(i)
        l = len(ret)
        # check combin
        if l >= 2:
            temp = ret[-1] + ret[-2]
            if temp in comb_dict:
                ret.pop()
                ret.pop()
                i = comb_dict[temp]
                ret.append(i)

        # check rev
        if i in rev_dict:
            temp = rev_dict[i]
            if temp in ret:
                ret = []

    return ''.join(ret)

if __name__ == '__main__':
    for no, line in enumerate(sys.stdin):
        if no == 0: continue
        f = line.split()
        nCombine = int(f[0])
        pos = 1
        combine = f[pos:(pos+nCombine)]
        pos += nCombine
        nRev = int(f[pos])
        pos += 1
        rev = f[pos:(pos+nRev)]
        pos += nRev
        query = f[pos+1]
        combine_dict = dict()
        for i in combine:
            combine_dict[i[0:2]] = i[2]
            combine_dict[i[1]+i[0]] = i[2]
        rev_dict = dict()
        for i in rev:
            rev_dict[i[0]] = i[1]
            rev_dict[i[1]] = i[0]

        #print  nCombine, combine, nRev, rev, query
        #print translate(combine_dict, rev_dict, query)
        print "Case #%d: [%s]" % (no, ', '.join(translate(combine_dict, rev_dict, query)))
        
