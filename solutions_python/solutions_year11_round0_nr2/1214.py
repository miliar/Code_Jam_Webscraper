#!/usr/python
#encoding=utf-8
import sys  
def oppose(opposed_letters, list):
    a = list[-1]
    for o in opposed_letters :
        if  o[1] == a  or  o[0] == a:
            if o[0] == a :        
                if o[1] in list :
                    list[:] = []
                    return                    
            else:                
                if o[0] in list :
                    list[:] = []
                    return
def fr(eb, a, b):
    for e in eb:
        if (e[0] == b and e[1] == a) or (e[0] == a and e[1] == b) :
            return e[2]
    return None                                      
file = open(sys.argv[1], "r")
lines  = file.readlines()
base    = ("Q", "W", "E", "R", "A", "S", "D", "F")
nb_case = lines[0].strip("\n")
lines.pop(0)
for k,l in enumerate(lines):
    lines[k] = l.strip("\n")    
for k, line in enumerate(lines):
    line = line.split()    
    eb  = line[1:int(line[0])+1]
    line = line[int(line[0])+1:]    
    opposed_letters = line[1:int(line[0])+1]
    line = line[int(line[0])+1:]
    to_invoke = line[1:][0]    
    resultat = []    
    for elem in to_invoke:        
        if len(resultat) < 1 :
            resultat.append(elem)            
        else :
            if (resultat[-1] in base) and (elem in base):
                neww = fr(eb, resultat[-1], elem)
                if neww :
                    resultat[-1:] = neww
                else :
                    resultat.append(elem)                    
            else :
                resultat.append(elem)            
            oppose(opposed_letters, resultat)    
    print "Case #%d: [%s]" %(k+1, ", ".join(resultat))
file.close()