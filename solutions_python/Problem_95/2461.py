'''
Created on Apr 13, 2012

@author: mdoan
'''


rev = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'de kr kd eoya kw aej tysr re ujdr lkgc jv']

ori = ['our language is impossible to understand',
'there are twenty six factorial possibilities',
'so it is okay if you want to just give up']

mymap = {}
for i in range(3):
    for j in range(len(rev[i])):
        mymap[rev[i][j]] = ori[i][j]
#rev_c = ''
#ori_c = ''
#for i in range(26):
#    if not chr(ord('a') + i) in ''.join(rev):
#        rev_c = chr(ord('a') + i)
#        print('rev: ', rev_c)
#    if not chr(ord('a') + i) in ''.join(ori):
#        ori_c = chr(ord('a') + i)
#        print('ori: ', ori_c)
#mymap[rev_c] = ori_c
mymap['q'] = 'z'
mymap['z'] = 'q'      
mymap['\n'] = '\n'
with open('input.txt') as f, open('output.txt', 'w') as fout:
    lines = [line for line in f]
    n = int(lines[0])
    for i in range(n):
        res = ''.join(mymap[elem] for elem in lines[i+1] if elem != '\n')
        print('Case #' + str(i+1) + ': ' + res, file = fout)
