#! /usr/bin/env python
#coding=utf-8


import sys

def main():
    if len(sys.argv) < 2:
        return
    f = open(sys.argv[1], "r").read().splitlines()
    t = int(f[0])
    del f[0]
    for i in xrange(1, t + 1):
        n = int(f[0])
        del f[0]
        map = []
        for j in xrange(n):
            map.append(list(f[0]))
            del f[0]
        print "Case #%d:"  % i
        wp = [0 for _ in xrange(n)]
        for j in xrange(n):
            win = 0
            comp = 0
            for k in xrange(n):
                if map[j][k] == '1':
                    win += 1                    
                if map[j][k] != '.':
                    comp += 1
            wp[j] = (win + 0.0) / comp
        wpx = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for pk in xrange(n):
            for j in xrange(n):
                win = 0
                comp = 0
                for k in xrange(n):
                    if k == pk:
                        continue
                    if map[j][k] == '1':
                        win += 1
                    if map[j][k] != '.':
                        comp += 1
                wpx[pk][j] = (win + 0.0) / comp
        owp = [0 for _ in xrange(n)]
        for j in xrange(n):
            wps = 0.0
            comp = 0
            for k in xrange(n):
                if map[j][k] != '.':
                    wps += wpx[j][k]
                    comp += 1
            owp[j] = wps / comp
        oowp = [0 for _ in xrange(n)]
        for j in xrange(n):
            owps = 0.0
            comp = 0
            for k in xrange(n):
                if map[j][k] != '.':
                    owps += owp[k]
                    comp += 1
            oowp[j] = owps / comp
        for j in xrange(n):
            print 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]
        
if __name__ == '__main__':
    main()
