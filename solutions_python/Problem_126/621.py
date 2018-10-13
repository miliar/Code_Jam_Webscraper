import os, sys, math, time
from operator import itemgetter, attrgetter

vowels = ['a','e','i','o','u']

def lingua(name, length):
	value = []
	nameval = 0
	num = 0
	pituus = len(name)-1
	values = {}
	for l in range (0, len(name)):
		if name[l] in vowels:
			value.append(0)
			num = 0
		else:
			value.append(1)
			num = num +1
			if num >= length:
				before = 1+l-length
				after = pituus-l
				for x in range(l-before, l+1):
					for y in range(l, l+after+1):
						a = (str(x)+str(y))
						values.update({a:0})
						nameval = nameval + 1

				#print before, after
	#print values
	print ''.join(map(str, value))
	#print name[0], name[len(name)-1]
	return len(values)



try:
	file = sys.argv[1]
except Exception as inst:
	print inst, '\n\nSyota avattava tiedosto parametrina!\n\n'
else:
	file = sys.argv[1]
	fin = open(file, 'r')
	fout = open(file[:-2]+'out', 'w')
	cases = fin.readline()
	print 'tapauksia ' + cases

	start = time.clock()
	for case in range(0, int(cases)):
		name, length = fin.readline()[:-1].split(' ')
		length = int(length)

		value = lingua(name, length)

		print name, length

		print 'nimen arvo:', value, '\n'
		print ('Case #'+str(case+1)+': '+ str(value) +'\n')
		fout.write('Case #'+str(case+1)+': '+ str(value) +'\n')


	print 'time:', time.clock() - start
	fin.close()
	fout.close()
