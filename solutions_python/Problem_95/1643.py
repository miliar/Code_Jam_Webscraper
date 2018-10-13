import sys

code = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
enco = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

mapping = {}

mapping['z'] = 'q'
mapping['q'] = 'z'

for i in range(len(code)):
	mapping[code[i]] = enco[i]

#print len(mapping.keys()), sorted(mapping.keys()), '\n', sorted(mapping.values())

lines = open(sys.argv[1], 'rt').readlines()

count = 1
for l in lines[1:]:
	ss = l.strip()
	rr = ''
	
	for c in ss:
		rr += mapping[c]

	print 'Case #%d: %s' % (count, rr)
	
	count += 1