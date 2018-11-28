#! /usr/bin/env python
#coding=utf-8

import sys
def main():
    if len(sys.argv) < 2:
        return
    f = open(sys.argv[1], "r").read().splitlines()
    t = int(f[0])
    for i in xrange(1, t + 1):
        combine = {}
        opposed = {}
        
        z = f[i]
        s = z.split()
        c = int(s[0])
        del s[0]
        for j in xrange(c):
            combine.update({s[0][1::-1]:s[0][2], s[0][:2]:s[0][2]})
            del s[0]
        d = int(s[0])
        del s[0]
        for j in xrange(d):
            opposed.update({s[0][0]:s[0][1], s[0][1]:s[0][0]})
            del s[0]
        n = int(s[0])
        r = s[1][:n]
        
        ret = []
        for j in r:
            #print j, ret, 
            if ret:
                t = "%s%s" % (ret[-1], j)
                if t in combine:
                    ret = ret[:-1]
                    ret.append(combine[t])
                else:
                    if j in opposed and opposed[j] in ret:
                        ret = []
                    else:
                        ret.append(j)
            else:
                ret.append(j)
            #print ret
        print "Case #%d: [%s]" % (i, ", ".join(ret))

if __name__ == '__main__':
    main()
