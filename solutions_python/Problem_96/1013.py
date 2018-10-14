#! /usr/bin/env python
# -*- coding: utf8 -*-

def do_calc(line):
    (n,s,p) = line[:3]
    t = line[3:]
    result = 0
#    print "\n",n,s,p,t
    for i in range(n):
        nb = p + max(p-1,0)*2
        sb = p + max(p-2,0)*2
#        print i,t[i], '#', nb, '#', sb
        if t[i] >= nb:
#            print 'Normal Pass'
            result += 1
        elif t[i] >= sb and s > 0:
            s -= 1 
            result += 1
#            print 'Surprise Pass'
    return result

def main():
    for t in range(input()):
        line = map(int,raw_input().split())
        print 'Case #%d: %d' % ( t+1, do_calc(line) )

if __name__ == '__main__':
    main()
