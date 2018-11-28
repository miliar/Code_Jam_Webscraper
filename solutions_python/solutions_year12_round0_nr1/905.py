'''
Created on Apr 13, 2012

@author: Phil
'''
'''
Created on May 6, 2011

Google Code Jam

user: philipbo

@author: Phil Bozak
'''

def transWord(word):
    d = { 'a': 'y', 'b': 'h', 'c': 'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
    rw = [" " for a in range(len(word))]
    for c in range(len(word)):
        rw[c] = d[word[c]]
    
    return ''.join(rw)


import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0] #filename (without the extension)

fr = open(namefile+'.in', 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])

for casenum in range(1,numCases+1):
    words = lines[casenum].split(' ')
    nwords = []
    for e in words:
        nwords.append(transWord(e))
    outs = ""
    for w in nwords:
        outs += w+" "
    #outs = outs[:-1]
    output += "Case #"+str(casenum)+": "+outs+"\n"

output=output[:-1]
fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()