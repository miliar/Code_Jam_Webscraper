#! /usr/bin/env python

def toMin(a):
    min = 0    
    m = []
    m = a.split(':')
    min += int(m[0])*60
    min += int(m[1])
    return min 


n = input()
for i in range(0, n):
    
    ta = 0
    tb = 0
    nas = []
    ns = []    
    oa = []
    ob = []


    tat = input()
    ns = raw_input().split(' ')

    #print tat

    for j in range(0, int(ns[0])):
        aux = raw_input().split(' ')
        aux.append('A')
        nas.append(aux)
    for j in range(0, int(ns[1])):
        aux = raw_input().split(' ')
        aux.append('B')
        nas.append(aux)
    
    nas.sort()
    
    #print "Todos:" + str(nas)
    for j in nas:
        if j[2] == 'A':
            if len(oa) == 0:
                ta += 1
                ob.append(j)
            else:            
                for k in oa:
                    if toMin(k[1])+tat <= toMin(j[0]):
                        oa.remove(k)
                        #print "Aproveitou b-a: " + str(k)
                        ta -= 1
                        break
                ta += 1
                ob.append(j)
            

        else:
            if len(ob) == 0:
                tb += 1
                oa.append(j)
            else:
                for k in ob:
                    if toMin(k[1])+tat <= toMin(j[0]):
                        ob.remove(k)
                        #print "Aproveitou a-b: " + str(k)
                        tb -= 1
                        break
                tb += 1
                oa.append(j)
        #print "ta = " + str(ta)
        #print "tb = " + str(tb)
        #print "Em A:" + str(oa)
        #print "Em B:" + str(ob)

    print "Case #"+str(i+1)+": "+ str(ta) +  " " + str(tb)
            
                
    


