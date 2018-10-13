from string import lowercase
import sys
enc = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z'
ori = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q'

dic = {}

for idx in range(0, len(enc)):
	dic[enc[idx]] = ori[idx]
	
inp = sys.stdin.readlines()
T = int(inp[0])

for i in range(0, T):
	res = ''
	for letter in inp[i + 1]:
		if letter == '\n':
			continue
		
		res = res + dic[letter]

	print 'Case #%d: %s' % (i + 1, res)
	