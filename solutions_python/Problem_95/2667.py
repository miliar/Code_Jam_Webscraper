def mapKeys(cipher, raw, b):

	for i in range(len(raw)):
		if i in b:
			print 'Key ', i, ' is present'

		b[cipher[i]] = raw[i]

	return b


if __name__ == '__main__':

	keys = {}

	keys['z'] = 'q'
	keys['q'] = 'z'

	onec = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
	oner = 'our language is impossible to understand'
	keys = mapKeys(onec, oner, keys)
	onec = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
	oner = 'there are twenty six factorial possibilities'
	keys = mapKeys(onec, oner, keys)
	onec = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
	oner = 'so it is okay if you want to just give up'
	keys = mapKeys(onec, oner, keys)


	fin = open('in', 'r')
	fout = open('out', 'w')

	ans = []

	fin.readline()

	while 1:
		line = fin.readline()

		if not line:
			break

		temp = line.split()
		str = []

		for i in temp:
			for j in i:
				str.append(keys[j])
			str.append(' ')

		ans.append(''.join(str[:len(str) - 1]))

		del str[:]

	for i in range(len(ans)):
		fout.write('Case #%d: %s\n' % (i + 1, ans[i]))
