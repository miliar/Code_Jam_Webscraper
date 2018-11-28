from sys import argv

f = open( argv[1] )
for i in xrange(int(f.readline())):
    line = f.readline().split()
       
    a = 0
    combo = {}
    for b in xrange(int(line[a])):
        a += 1
        combo[ line[a][0:2] ] = line[a][2]
    oppose = []
    a += 1
    for b in xrange(int(line[a])):
        a += 1
        oppose.append( line[a] )
           
   
    spell = []
    for ch in line[a+2]:
        if len(spell) == 0:
            spell.append( ch )  
        elif ch+spell[-1] in combo.keys():
            t = spell[-1]
            spell.pop()
            spell.append( combo[ ch+t ] )
        elif spell[-1]+ch in combo.keys():
            t = spell[-1]
            spell.pop()
            spell.append( combo[ t+ch ] )
        else:
           
            test = False
            for el in spell: 
                if el+ch in oppose or ch+el in oppose:
                    test = True                
            if test:
                spell = []       
            else:
                spell.append( ch )
        
        out = ''        
        if len(spell) == 0:
            out = '[]'
        else:
            for el in spell:
                out += el + ', '
            out = '['+out[:-2] + ']'        

    print "Case #"+str(i+1)+": "+out
f.close()
