
translate = dict()
enc = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
dec = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for i in range(len(enc)):
	translate[enc[i]] = dec[i]
translate['q'] = 'z'
translate['z'] = 'q'

#for c in "abcdefghijklmnopqrstuvwxyz":
#	if c not in translate.keys():
#		print "Manca "+c

fin = open('input.txt', 'r')
num = int(fin.readline())
for i in range(num):
	line = fin.readline()[:-1]
	plain = ""
	for char in line:
		if char in translate.keys():
			plain += translate[char]
		else:
			plain += char
	print "Case #%d: %s" % (i+1, plain)
