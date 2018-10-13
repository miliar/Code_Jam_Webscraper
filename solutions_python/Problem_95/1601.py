#!/usr/bin/python

from array import array

if __name__=="__main__":
	destStr = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q"
	srcStr = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z"
	transMap = array('c', [chr(0)]*(ord('z')-ord('a')+1))
	for i in range(len(destStr)):
		if ord(destStr[i])>=ord('a') and ord(destStr[i])<=ord('z'): 
			transMap[ord(destStr[i])-ord('a')] = srcStr[i]
	for i in range(len(transMap)):
		if (ord(transMap[i])==0):
			transMap[i]='q'
	#print transMap

	for i in range(int(raw_input())):
		str = raw_input()
		origStr = ""
		for char in str:
			if ord(char)>=ord('a') and ord(char)<=ord('z'): 
				origStr += transMap[ord(char)-ord('a')]
			else:
				origStr += char
		print "Case #%d: %s" %(i+1, origStr)

