import sys

def doStuff(path):

	in_f = open(path)


	mt = int(in_f.readline())
	t = mt


	while (t):
		r = int(in_f.readline())
		r -= 1

		h1 = {}
		for i in range(4):
			l = in_f.readline()

			if i == r:
				l = l.split(' ')

				for n in l:
					h1[int(n)] = 1


		r = int(in_f.readline())
		r -= 1



		h2 = []
		for i in range(4):
			l = in_f.readline()

			if i == r:
				l = l.split(' ')

				for n in l:
					n = int(n)
					if not n in h1:
						continue
					if h1[n] == 1:
						h2.append(n)


		if len(h2) == 0:	
			print('Case #%d: Volunteer cheated!'%(mt - t + 1))

		if len(h2) == 1:
			print('Case #%d: %d'%(mt - t +1, h2[0]))

		if len(h2) > 1:
			print('Case #%d: Bad Magician!'%(mt - t +1))


		t -= 1



if __name__ == '__main__':
	doStuff(sys.argv[1])
