#Google Code Jam 2012 - Qualification A
#Victor Legros
with open('A-small-attempt0.in') as f:
    with open ('A-small-attempt0.out', 'w') as out:
        googDict = {' ': ' ', 'y': 'a', 'e': 'o', 'q': 'z'} #Given

        #inelegant, but why not?
        #trial and error based on input
        googDict['j'] = 'u'
        googDict['p'] = 'r'
        googDict['m'] = 'l'
        googDict['y'] = 'a'
        googDict['s'] = 'n'
        googDict['l'] = 'g'
        googDict['c'] = 'e'
        googDict['k'] = 'i'
        googDict['d'] = 's'
        googDict['x'] = 'm'
        googDict['v'] = 'p'
        googDict['n'] = 'b'
        googDict['r'] = 't'
        googDict['i'] = 'd'
        googDict['b'] = 'h'
        googDict['t'] = 'w'
        googDict['a'] = 'y'
        googDict['h'] = 'x' 
        googDict['w'] = 'f'
        googDict['f'] = 'c'
        googDict['o'] = 'k'
        googDict['u'] = 'j'
        googDict['g'] = 'v'
        googDict['z'] = 'q' #only this is not given from examples
        
        T = int(f.readline().strip())
        for i in range(T):
            G = f.readline().strip()
            temp = ''
            for j in range(len(G)) :
                if G[j] in googDict :
                    temp += googDict[G[j]]
                else :
                    temp += '.'

            

            #print('Case #' + str(i+1) + ': ' + str(temp))
            out.write('Case #' + str(i+1) + ': ' + str(temp) + '\n')
        #print(sorted(googDict.keys()))
        #print(sorted(googDict.values()))
    out.close()
f.close()
