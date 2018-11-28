horz0 = []
horz1 = []
horz2 = []
horz3 = []
vert0 = []
vert1 = []
vert2 = []
vert3 = []
winctr = 0
dotcnt = 0
didwin = 0
i = 0
casectr = 1

output = open('OutFile', 'a')

with open('A-large.in', 'r') as inputFile:
    for line in inputFile:  
        
        if i == 0:
            pass
        
        elif i == 4:
            
            
            horz3 = line
            vert0.append(line[0])
            vert1.append(line[1])
            vert2.append(line[2])
            vert3.append(line[3])
            
            for k in (horz0, horz1, horz2, horz3):
                for j in ('X','O'):
                    if k.count(j) > 3 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                    elif k.count(j) == 3 and k.count('T') == 1 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                if k.count('.') > 0:
                    dotcnt = dotcnt + 1
            
            for k in (vert0, vert1, vert2, vert3):
                for j in ('X','O'):
                    if k.count(j) > 3 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                    elif k.count(j) == 3 and k.count('T') == 1 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                if k.count('.') > 0:
                    dotcnt = dotcnt + 1
                        
            diag1 = (horz0[0],horz1[1],horz2[2],horz3[3])
            diag2 = (horz0[3],horz1[2],horz2[1],horz3[0])
            
            for k in (diag1, diag2):
                for j in ('X','O'):
                    if k.count(j) > 3 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                    elif k.count(j) == 3 and k.count('T') == 1 and didwin <1:
                        output.write('Case #'+str(casectr)+': '+str(j)+' won\n')
                        winctr = winctr + 1
                        didwin = didwin + 1
                        
            if winctr < 1 and dotcnt < 1:
                output.write('Case #'+str(casectr)+': Draw\n')
            if winctr < 1 and dotcnt > 0:
                output.write('Case #'+str(casectr)+': Game has not completed\n')
            
            winctr = 0
            dotcnt = 0
            didwin = 0
            casectr = casectr + 1
                
            
            horz0 = []
            horz1 = []
            horz2 = []
            horz3 = []
            vert0 = []
            vert1 = []
            vert2 = []
            vert3 = []
            
            i = -1

        
        elif i < 4:
            if i == 1:
                horz0 = line
            elif i == 2:
                horz1 = line
            elif i == 3:
                horz2 = line
            vert0.append(line[0])
            vert1.append(line[1])
            vert2.append(line[2])
            vert3.append(line[3])
            
        
        i = i + 1