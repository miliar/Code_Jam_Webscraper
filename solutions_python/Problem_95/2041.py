'''
Created on 14/04/2012

@author: michael
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz '
pt = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
ct = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

def translate_line(line):
    output = ''
    for char in line:
        output += inverted_lookupTable[char]
    return output
#build lookup table
lookupTable = {'a':'y', 'o':'e', 'z':'q', ' ':' '}
for i,char in enumerate(pt):
    lookupTable[char] = ct[i]
#verify lookup table
missing1 = set()
missing2 = set()
for letter in alphabet:
    if letter not in lookupTable.keys():
        missing1.add(letter)
    if letter not in lookupTable.values():
        missing2.add(letter)
assert len(missing1) == len(missing2) == 1
lookupTable[missing1.pop()] = missing2.pop()
inverted_lookupTable = dict([[v,k] for k,v in lookupTable.items()])
#read in input
inFile = open('A-small-attempt0.in','r')
outFile = open('A-small-attempt0.out','w')

noCases = int(inFile.readline().strip())

for i in range(noCases):
    if i < noCases - 1:
        outFile.write('Case #'+ str(i+1) +': ' + translate_line(inFile.readline().strip()) + '\n') 
    else:
        outFile.write('Case #'+ str(i+1) +': ' + translate_line(inFile.readline().strip()))
inFile.close()
outFile.close()