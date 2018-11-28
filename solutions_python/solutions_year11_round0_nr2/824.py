#!/usr/bin/env python
#-*- coding: utf-8 -*-

def magicka(data):
    data = data.split(" ")
    data.reverse()

    comb = list()
    oppo = list()

    for i in range(int(data.pop())):
        s = data.pop()
        comb.append(((s[0], s[1]), s[2]))

    for i in range(int(data.pop())):
        s = data.pop()
        oppo.append((s[0], s[1]))
    
    data.pop()
    
    output = list()
    
    for c in data.pop():
        combflag = False
        oppoflag = False
        
        if output:
            for i, t in comb:
                if sorted(i) == sorted((c, output[-1])):
                    output[-1] = t
                    combflag = True
                    break
        
        if not combflag:
            for i in oppo:
                if c in i:
                    l = list(i)
                    l.remove(c)
                    if l[0] in output:
                        output = list()
                        oppoflag = True
                        break
                
            if not oppoflag:
                output.append(c)
    
    return "[%s]" % ", ".join(output)

if __name__ == "__main__":
    n = int(raw_input())
    
    for i in range(n):
        print "Case #%d: %s" % (i + 1, magicka(raw_input()))
