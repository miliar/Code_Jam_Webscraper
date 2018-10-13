'''
Created on April 14, 2012

@author: indra
'''
import sys, os

filename = "A-small-attempt0"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

ip="qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
op="zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
alpha="abcdefghijklmnopqrstuvwxyz"
missingL={}
missingR={}
for ch in alpha:
	missingL[ch]=None
	missingR[ch]=None
	
map={}
for i in range(len(ip)):
	map[ip[i]]=op[i]

for key in map.iterkeys():
	if missingL.has_key(key):
		missingL.pop(key)
	#print "--",key, map[key]
	if missingR.has_key(map[key]):
		missingR.pop(map[key])

print missingL, missingR
#print ar
map['z']='q'
map[' ']=' '

cases = int(reader.readline().rstrip())

#print cases

caseno = 1
while caseno<=cases:
	case = reader.readline().rstrip()
	op=""
	for ch in case:
		op = op + map[ch]

	writer.write("Case #"+str(caseno)+": "+op+"\n")
	caseno+=1


writer.close()