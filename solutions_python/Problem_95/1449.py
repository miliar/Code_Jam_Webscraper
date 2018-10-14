import string, sys

mapping = dict((a, b) for a, b in zip(
	"""ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqeez""",
	"""our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzooq"""
) if a in string.ascii_lowercase and b in string.ascii_lowercase)

print [x for x in string.ascii_lowercase if x not in mapping]

sys.stdin = open('tounges.in')
sys.stdout = open('tounges.out', 'w')

for i in range(input()):
	print "Case #%d: %s" % (i + 1, ''.join(mapping[c] if c in mapping else c for c in raw_input()))