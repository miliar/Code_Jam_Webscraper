filename = "C-large"

f = open("%s.in"  %filename)
o = open("%s.out" %filename, 'w')

cases = int(f.readline())

def pAdd(candies):
	l = len(candies[0])
	r = ['0'] * l

	for c in candies:
		for i in range(l):
			if r[i] != c[i]:
				r[i] = '1'
			else:
				r[i] = '0'

	r = ''.join(r)
	return int(r,2)

def sAdd(candies):
	r = 0
	for c in candies:
		r += int(c, 2)

	return r


for case in range(cases):
	res = ''
	
	numCandies = int(f.readline())
	print "Numcandies", numCandies
	#create nice aligned binary strings
	candies = [bin(int(i))[2:] for i in f.readline().split(" ")]
	m = max([len(i) for i in candies])
	candies = [i.zfill(m) for i in candies]
	
	if pAdd(candies) != 0:
		res = "NO"
	else: # try to find the right distribution
		candies.sort(reverse=True)
		tr = 1
		while True:
			dist = {'P':[], 'S':[]}
			b = bin(tr)[2:].zfill(numCandies)
			for c in range((numCandies-1),-1,-1):
				if b[c] == '1':
					dist['P'].append(candies[c])
				else:
					dist['S'].append(candies[c])
			if pAdd(dist['P']) == pAdd(dist['S']):
				res = str(sAdd(dist['S']))
				break
			tr += 1

	o.write("Case #%d: %s\n" %(case+1, res))
	

o.close()
f.close()