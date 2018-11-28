import sys

if __name__ == '__main__':
	googlerese_ex = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
	english_ex = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

	googlerese_dict = dict(zip(list(googlerese_ex), list(english_ex)))
	googlerese_dict['z'] = 'q'
	googlerese_dict['q'] = 'z'

	# print googlerese_dict

	f = open(sys.argv[1], 'r')

	t = f.readline()

	i = 1
	for line in f.readlines():
		line = line.replace('\n', '')
		translated = ''
		for char in line:
			if char == ' ':
				translated += ' '
			else:
				translated += googlerese_dict[char]

		print "Case #{}: {}".format(i, translated)
		i += 1