#!/usr/bin/python

import sys
import math

if __name__=="__main__":
    data = sys.stdin.readlines()
    number = int(data[0])
    for times in xrange(0, number):
        print "Case #%d:" % (times+1),
        line = data[times+1].split(' ')
        comb,oppo,res = [],[],[]
        
        c = int(line[0])
        for i in range(1,c+1):
            comb.append((line[i][0:2], line[i][2]))
        line = line[c+1:]
        
        d = int(line[0])
        for i in range(1,d+1):
            oppo.append(line[i])
        line = line[d+1:]
        
        n = int(line[0])
        ops = line[1][:-1]
        rule,last_rule = "",""

        for op in ops:
            if len(res) == 0:
                res.append(op)
            else:
                s = [res[-1]+op, op+res[-1]]
                flag = True
                
                for c in comb:
                    if s[0] == c[0] or s[1] == c[0]:
                        res[-1] = c[1]
                        rule = last_rule
                        flag = False
                        break
                if not flag:
                    continue
                
                if op in rule:
                    res = []
                    rule = ""
                    last_rule = ""
                    continue

                res.append(op)
            
            last_rule = rule
            for d in oppo:
                if op == d[0]:
                    rule += d[1]
                elif op == d[1]:
                    rule += d[0]
                        
        print str(res).replace("'", '')
