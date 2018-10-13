googlerese = []
googlerese.append('ejp mysljylc kd kxveddknmc re jsicpdrysi')
googlerese.append('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
googlerese.append('de kr kd eoya kw aej tysr re ujdr lkgc jv')
english = []
english.append('our language is impossible to understand')
english.append('there are twenty six factorial possibilities')
english.append('so it is okay if you want to just give up')
translate_dict = {}
for i in xrange(len(googlerese)):
	for j in xrange(len(googlerese[i])):
		if translate_dict.setdefault(googlerese[i][j]) == None:
			translate_dict[googlerese[i][j]] = english[i][j]
translate_dict['q'] = 'z'
translate_dict['z'] = 'q'
#print translate_dict
#print len(translate_dict)
T = int(raw_input())
for i in xrange(T):
	line = raw_input()
	newline = ''
	for each in line:
		newline += translate_dict[each]
	print 'Case #%d: %s' % (i + 1, newline)
