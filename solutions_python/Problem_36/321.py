#!/usr/bin/env python

import re

def findit(m, i, letter_index):
    
    if i >= len(m):
        return 1
    else:
        total = 0
        for l in range(0,len(m[i])):

            if letter_index < m[i][l]:
                total = total + findit(m,i+1,m[i][l])
            
        return total
    return 0

def printMatrix(m):
    
    for i in range(0,len(m)):
        print m[i]
    
    print "--------------------------------"       

f = open("WelcomeToCodeJam/sample.in",'r')

try:
    cj = "welcome to code jam"
    cj_r = ""
    for i in range(0,len(cj)):
        cj_r = cj_r + "%s[\w\W ]*" % cj[i]
    cj_r = "[" + cj_r + "]*"
    

    r = re.compile(cj_r)
    
    while f:
        
        cases = int(f.next().rstrip("\n"))
        
        for i in range(0,cases):
            line = f.next().rstrip("\n").lower()

            line = line[line.find("w"):len(line)]
            line = line[0:line.rfind("m")+1]

            r2 = re.compile("[^welcometocodejam ]+")
            line = r2.sub("",line)
           
            
            m = []
            
            for l in cj:
                m_l = []
                r2 = re.compile(l)
                for r2_r in r2.finditer(line):
                    m_l.append(r2_r.start())
                m.append(m_l)
            
            #printMatrix(m)
            
            total = findit(m,0,-1)
            
            total = str(total % 10000)
            
            for l in range(0,4-len(total)):
                total = "0" + total
            
            print "Case #%s: %s" % (i+1,total)
        
                
    
        
except Exception, e:
    #pass
    print e
finally:
    f.close()