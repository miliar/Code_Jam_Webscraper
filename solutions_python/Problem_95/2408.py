#!/usr/bin/env python

dictionary = {'a': 'y', ' ': ' ', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g':
'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o':
'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w':
't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}
inverted_dic={}
for k,v in dictionary.items():
  inverted_dic.update({v:k})

loop=int(raw_input())
result=''
for i in range(loop):
  s=raw_input();
  result+='Case #%d: ' % (i+1)
  r=''
  for i in s:
    r+=inverted_dic[i]
  r+="\n"
  result+=r

print result
