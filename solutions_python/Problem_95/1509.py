# -*- coding: utf-8 -*-
import sys


sgle = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
sore = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

tran = {}

for i in xrange(len(sgle)) :
	tran[sgle[i]] = sore[i]

tran["z"] = "q"
tran["q"] = "z"

qNum = int(sys.stdin.readline()[0:-1])

for q in xrange(qNum):

	line = sys.stdin.readline()[0:-1]

	ans = ""
	for s in line:

		ans += tran[s] 
	
	print "Case #" + str(q+1) + ": " + ans



