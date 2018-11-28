#!/usr/bin/env python

import sys

f=open(sys.argv[1])
outp = open(sys.argv[1]+'.out.txt','w')
T=int(f.next())
dic = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
cnt=0
while cnt < T:
	cnt+=1
	cipher = f.next()
	plaintxt = ''
	for x in cipher:
		if x in dic:
			plaintxt+=dic[x]
		else:
			plaintxt+=x
	print 'Case #'+str(cnt)+': '+plaintxt
	outp.write('Case #'+str(cnt)+': '+plaintxt)
outp.close()
