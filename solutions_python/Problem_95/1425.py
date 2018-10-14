#!/usr/bin/env python2


s1 = " qzejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
s2 = " zqourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"


r = {}

for i in range(len(s1)):
	r[s1[i]] = s2[i]
'''
r2 = {}

for i in range(len(s1)):
	r2[s2[i]] = s1[i]

for k,v in sorted(r.items()):
	print k, v


for k,v in sorted(r2.items()):
	print k, v
exit()
'''


c = int(raw_input())
x = c
while (c):
	d = []
	c = c - 1
	frase = (raw_input())
	frase2 = ""
	for i in range(len(frase)):
		frase2 += r[frase[i]]
	print "Case #"+str(x-c)+": "+frase2
