#!/usr/bin/env python
#-*- coding:utf-8 -*-

filename = 'B-large.in'
file=open(filename)

'''
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
'''

'''
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
'''

for case in range(int(file.readline())):
    
    # wczytaj linię
    line=file.readline().split()
#    print line
    
    c_nr = int(line.pop(0))
    c=dict()
    
    # niech c będzie listą tupli ('AB', 'C') - to nie powinna być lista tylko słownik ex: c['EG']='J'
    for i in range(c_nr): 
        tri = line.pop(0)
        c[tri[0:2]]=tri[-1]
        c[tri[1]+tri[0]]=tri[-1]
#        c.append( (tri[0:2], tri[-1]) )
#        c.append( (tri[1]+tri[0], tri[-1]) )
        
    
    # d to powinien być set albo dict
    d_nr = int(line.pop(0))
    d=set()
    for i in range(d_nr):
        two=line.pop(0)
        
        d.add(two)
        d.add(two[::-1])
    
#    print c, d

    zaklecie = list(line.pop())
#    print 'zaklecie : %s' % zaklecie
    
    # najpierw wywołujemy/invoke elementy - czyli sprawdzamy czy są w c
    # potem sprawdzamy czy nie są przeciwne - czy są w d - jak są to usuwamy
    # idziemy od początku do końca zaklęcia
    
    output = []
    
    while len(zaklecie)>0:
        output.append(zaklecie.pop(0))    
        
        if len(output)<2:
            continue
        
        # najpierw sprawdzamy czy ostatnie 2 elementy są w c, i wtedy łączymy je w inny 
        last_two = output[-2] + output[-1]
        if last_two in c:
            # musimy ostatnie 2 elementy zamienić na jeden inny
            output = output[:-2] 
            output.append(c[last_two])
            
            continue    # przeskakujemy kasowanie
        
        
        # teraz sprawdzamy czy ostatni element razem z jakimś innym poprzednim tworzą element z listy d, jak tak to kasujemy całość
        if len(output)<2: continue
        
        for letter in output[:-1]:                
            if letter+output[-1] in d:
                output=[]
                break
    
    
    # Case #4: [Z, E, R, A]
    print 'Case #%i: %s' % ( case+1, '[' + ', '.join(output) + ']')
    
#!/usr/bin/env python
#-*- coding:utf-8 -*-


