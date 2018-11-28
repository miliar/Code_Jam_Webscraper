#!/usr/bin/python

d = {
'y':'a',
'n':'b',
'f':'c',
'i':'d',
'c':'e',
'w':'f',
'l':'g',
'b':'h',
'k':'i',
'u':'j',
'o':'k',
'm':'l',
'x':'m',
's':'n',
'e':'o',
'v':'p',
'z':'q',
'p':'r',
'd':'s',
'r':'t',
'j':'u',
'g':'v',
't':'w',
'h':'x',
'a':'y',
'q':'z'}

def compute():
  s = raw_input()
  ret = ""
  for i in s:
    if i == ' ':
      ret+=i
    else:
      ret+=d[i]
  return ret

n = int(raw_input())
for i in range(0,n):
  print "Case #%d: "%(i+1)+str(compute())
