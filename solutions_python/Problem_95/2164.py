#!/usr/bin/env python





map1={' ':' ','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
def mapper(k):
   return map1[k]

f=open('A-small-attempt0.in','r')
f1=open('output.txt','w')
n=int(f.readline())
for i in xrange(n):
   line=f.readline().strip()
   line=''.join(map(mapper,line))
   f1.write("Case #%d: %s\n"%(i+1,line))
f.close()
f1.close()
