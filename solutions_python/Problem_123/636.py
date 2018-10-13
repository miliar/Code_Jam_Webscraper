import os, sys, math, time
from operator import itemgetter, attrgetter

def osmos(mote, lista, pos, count = 0, smallest = math.pow(10,6)):
	#print pos, len(lista)
	if pos >= len(lista): #reached to end
		return count
	if mote < 2: #mote small, end
		return len(lista)
	if mote > lista[pos]: #freeride with eating
		#print 'eat', mote, lista[pos]
		return osmos(mote+lista[pos], lista, pos+1, count, smallest)
	else: # iterative depth search
		num = osmos(mote+mote-1, lista, pos, count+1, smallest) #add mote
		if num < smallest:
			smallest = num
		num = osmos(mote, lista, pos+1, count+1, smallest) #delete list pos
		if num < smallest:
			smallest = num

		return smallest



try:
	file = sys.argv[1]
except Exception as inst:
	print inst, '\n\nSyota avattava tiedosto parametrina!\n\n'
finally:
	file = sys.argv[1]
	fin = open(file, 'r')
	fout = open(file[:-2]+'out', 'w')
	cases = fin.readline()
	print 'tapauksia ' + cases

	start = time.clock()
	for case in range(0, int(cases)):
		temp = fin.readline()[:-1].split(' ')
		mote = int(temp[0])
		num = int(temp[1])
		temp = sorted(map(int, fin.readline()[:-1].split(' ')))

		print mote, num
		print temp
		moves = osmos(mote, temp, 0)


		print ('Case #'+str(case+1)+': '+ str(moves) +'\n')
		fout.write('Case #'+str(case+1)+': '+ str(moves) +'\n')


	print 'time:', time.clock() - start
	fin.close()
	fout.close()
