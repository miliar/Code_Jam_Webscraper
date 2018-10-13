# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Shadow\.spyder2\.temp.py
"""

def checken(eintrag_aus_woerterbuch):
    temp = 0
    zwischensumme = 0
    for i in range(int(eintrag_aus_woerterbuch[0])):
        zwischensumme += int(eintrag_aus_woerterbuch[1][i])
        if (zwischensumme + temp) < i+1:
            temp = temp +((i+1)-(zwischensumme+temp))
    return temp

f = open('A-large.txt', 'r')

number_of_lines = int(f.readline())

output = dict()

woerterbuch = dict()

for i in range(number_of_lines):
    temp = f.readline().split()
    woerterbuch[i] = temp
    
f.close()
    
for i in range(number_of_lines):
    output[i] = checken(woerterbuch.get(i))

wf = open('output_comp_large.txt', 'w')

for i in range(number_of_lines):
    wf.write('Case #%s: %s\n' % ((i+1) , output.get(i)))

wf.close()