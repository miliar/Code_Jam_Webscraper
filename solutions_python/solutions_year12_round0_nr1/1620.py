cipher = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
text = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

alph = 'abcdefghijklmnopqrstuvwxyz'
mapping = {}
for ch in alph: mapping[ch] = ch
for idx, ci in enumerate(cipher):
	for idx2, ch in enumerate(ci):
		mapping[ch] = text[idx][idx2]
mapping['z'] = 'q'
mapping['q'] = 'z'

def trans(line):
	ret = ''
	for ch in line:
		ret += mapping[ch]
	return ret

f = open('A-small-attempt1.in')
lines = f.readlines()
for idx, line in enumerate(lines[1:]):
	print 'Case #%d: %s' % (idx + 1, trans(line.strip()))
