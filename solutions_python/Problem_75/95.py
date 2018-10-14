#!/usr/bin/python2.6

def testCase():
	data = iter(raw_input().split()).next

	combine = {}
	for _ in xrange(int(data())):
		item = data()
		combine[item[:2]] = combine[item[1]+item[0]] = item[2]

	oppose = {}
	for _ in xrange(int(data())):
		item = data()
		oppose.setdefault(item[0], set()).add(item[1])
		oppose.setdefault(item[1], set()).add(item[0])

	data()
	elements = ""
	for element in data():
		elements += element
		flag = False
		while len(elements) >= 2 and elements[-2:] in combine:
			elements = elements[:-2] + combine[elements[-2:]]
			flag = True
		if flag:
			continue
		if oppose.get(elements[-1], set()) & set(elements[:-1]):
			elements = ""
	return "[%s]" % (", ".join(elements),)

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %s" % (i + 1, testCase())
