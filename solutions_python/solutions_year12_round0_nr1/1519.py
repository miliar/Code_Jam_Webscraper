import collections
sampleIn = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvzq
"""
sampleOut = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upqz
"""
print sampleIn, sampleOut
inAlphabet = map(chr, range(97, 123))
outAlphabet = ['' for i in range(26)]

for c1, c2 in zip(sampleIn, sampleOut):
	charIndex = ord(c1) - 97
	if charIndex >= 0:
		outAlphabet = outAlphabet[:charIndex] + [c2] + outAlphabet[charIndex+1:]
outAlphabet = outAlphabet + [' ', '\n']
inAlphabet = inAlphabet + [' ', '\n']
charMap = {c1:c2 for c1, c2 in zip(inAlphabet, outAlphabet)}
print charMap

fIn = open('in.txt', 'rb')
fOut = open('out.txt', 'wb')
lIn = [line for line in fIn][1:]
decode = lambda source: map(lambda c: charMap[c], source)
lOut = [''.join(s)[:-1] for s in map(decode, lIn)]
for i, line in enumerate(lOut):
	fOut.write('Case #' + str(i+1) + ': ' + line + '\n')


