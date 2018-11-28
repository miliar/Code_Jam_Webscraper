import sys
import fileinput
s = "zyqee ejp mysljylc kd kxveddknmc re jsicpdrysi " + 	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" +	" de kr kd eoya kw aej tysr re ujdr lkgc jv"

f = "qazoo our language is impossible to understand " +"there are twenty six factorial possibilities "+"so it is okay if you want to just give up"

#print len(s), len(f)

dec = {}
for i in range(len(s)):
	dec[s[i]] = f[i]

#print sorted(dec.values())
for i in range(26):
	pass
	#print chr(i + ord('a')), dec[chr(i + ord('a'))]


f = open('A-small-attempt0.in', 'r')

numTests =  int(f.readline())

for i in range(numTests):
	encrypt = f.readline().strip()
	print "Case #" + str(i + 1) + ": " + ''.join(map(dec.get, encrypt))