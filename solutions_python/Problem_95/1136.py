#!/usr/bin/env python

import sys

## T test case
## G google string
## S output string
## Gstr sample google string 
## Sstr sample output string

##initial 
Gstr = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

Sstr = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

Dict = {}
for i in range(len(Gstr)):
	if (Gstr[i] not in Dict):
		Dict[ Gstr[i] ]=Sstr[i]
	elif (Dict [Gstr[i] ] != Sstr[i]):
		print "Error: Mapping ", Gstr[i], " is ", Dict[Gstr[i]], " not ", Sstr[i]

Dict['z'] = 'q'
Dict['q'] = 'z'
#keys = Dict.values()
#keys.sort()
#for i in range(len(keys)):
#	print keys[i], " : ", Dict[keys[i]] 
#print "the end"


# input and output
T = int( raw_input() )

for i in range(0, T):
	G = raw_input()
	S = ""
	for j in range(len(G)):
		S+=Dict[ G[j] ]

	print "Case #"+`i+1`+": "+S


