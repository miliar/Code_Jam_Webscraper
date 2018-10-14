#!/usr/bin/python
f = open('cjprelim1.txt','r')
op = open('cjprelim2.txt','w')
numLines = int(f.readline())
googlerese= {' ':' ', 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g','m':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

def replace_all(text, dic):
   for c in text:
       op.write(googlerese[c])
       
for i in range(numLines):
   op.write('Case #')
   op.write(str(i+1))
   op.write(': ')
   line = f.readline().strip()
   replace_all(line, googlerese)
   op.write('\n')
   

f.close()
op.close()
