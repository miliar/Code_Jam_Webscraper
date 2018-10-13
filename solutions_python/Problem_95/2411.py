#qwertyuiopasdfghjklzxcvbnm
#zfotwajdkrynscvxuigqmephbl

table = {
'q':'z',
'w':'f',
'e':'o',
'r':'t',
't':'w',
'y':'a',
'u':'j',
'i':'d',
'o':'k',
'p':'r',
'a':'y',
's':'n',
'd':'s',
'f':'c',
'g':'v',
'h':'x',
'j':'u',
'k':'i',
'l':'g',
'z':'q',
'x':'m',
'c':'e',
'v':'p',
'b':'h',
'n':'b',
'm':'l'
}

import sys

f = open('A-small-attempt0.in')
t = f.readlines()

t = t[1:]

nr = 1

for i in t:
  sys.stdout.write("Case #"+str(nr)+": ")
  for c in i:
    try:
      sys.stdout.write(table[c])
    except:
      sys.stdout.write(c)
  nr=nr+1
