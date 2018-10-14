#-*- coding:utf-8 -*-

DICT = {
'a': 'y',
'b': 'h',
'c': 'e',
'd': 's',
'e': 'o',
'f': 'c',
'g': 'v',
'h': 'x',
'i': 'd',
'j': 'u',
'k': 'i',
'l': 'g',
'm': 'l',
'n': 'b',
'o': 'k',
'p': 'r',
'q': 'z',
'r': 't',
's': 'n',
't': 'w',
'u': 'j',
'v': 'p',
'w': 'f',
'x': 'm',
'y': 'a',
'z': 'q',
' ': ' '}

def translate(stc):
    result = ''
    for letter in stc:
        result += DICT[letter]
    return result
        

f = open('test1.in')
r = f.readlines()
f.close()
print 'ok'
line = [i.rstrip('\n') for i in r]
cases = line[0]
results = ["Case #%s: %s\n" % (line.index(stc),translate(stc)) for stc in line[1:]]
print results
f = open('resultats.txt','w')
for i in results:
    f.write(i)
f.close()
