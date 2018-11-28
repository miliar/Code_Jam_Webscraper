#!/usr/bin/python
fname = 'A-small-attempt1.in'
fout = 'A-small-attempt1.out'
f = open(fname,'r')
lines = []
for line in f:
  lines.append(line)
f.close()

alphabet = {'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q',
' ':' '}

N = int(lines[0])
f2 = open(fout,'w')
for i in range(1,N+1):
  l = lines[i]
  l2 = "Case #"
  l2 += str(i)
  l2 += ": "
  for letter in l:
    for key,value in alphabet.iteritems():
      if key == letter:
        l2 += value
  l2 +="\n"      
  f2.write(l2)
  
f2.close()
  
          
