#!/usr/bin/env python

import re

f = open("AlienLanguage/sample.in",'r')

try:
   
    while f:
        
        line = f.next()
        
        parts = line.rsplit(" ")
        
        l = int(parts[0])
        d = int(parts[1])
        n = int(parts[2].rstrip("\n"))
        
        dictionary = []
        for i in range(0,d):
            dictionary.append(f.next().rstrip("\n"))
        
        case_num = 1
        for i in range(0,n):
            t = f.next().rstrip("\n")
            t = t.replace("(","[")
            t = t.replace(")","]")
            
            r = re.compile(t)
            
            count = 0
            
            for j in range(0,d):
                if r.match(dictionary[j]):
                    count = count + 1
            print "Case #%s: %s" % (case_num, count)
            case_num = case_num + 1
            

    
        
except Exception, e:
    #pass
    print e
finally:
    f.close()