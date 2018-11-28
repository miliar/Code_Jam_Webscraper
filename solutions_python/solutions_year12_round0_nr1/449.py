gogglese = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

english = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

mapping = {'a':'y', 'z':'q', 'q':'z'}

for i in xrange(len(gogglese)):
	g = gogglese[i]
	e = english[i]
	if g in mapping:
		if mapping[g] != e:
			print "ERROR in line", i, "!!!"
			print "g:", g
			print "e:", e
			print "mapping[g]:", mapping[g]
			print "gogglese[i:]:", gogglese[i:]
			print "english[i:]:", english[i:]
	else:
		mapping[g] = e

#print 'mapping:', mapping
#print 'mapping len:', len(mapping)

#print "letters taken: ", sorted(mapping.itervalues())

import sys
data = sys.stdin.readlines()

for ind, line in enumerate(data[1:]):
	#print line.split()
	print "Case #"+str(ind+1)+": "+" ".join(map(lambda word: "".join(map(lambda letter: mapping[letter], list(word))), line.split()))
