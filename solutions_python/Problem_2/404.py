import sys

def sumart(h,t):
	r = 0
	if h[1]+t >= 60:
		r = 1
	return ((h[0]+r)%24,(h[1]+t)%60)

# busca en s una hora menor a x
def buscarTren(s, x):
	for j in s:
		if j <= x:
			s.remove(j)
			return j
	return None

def tren(t,atob,btoa):
	trenes_en_B = []
	trenes_en_A = []
	trenesA = 0
	trenesB = 0
	
	atob.sort()
	btoa.sort()
	
	for i in atob:
		trenes_en_B.append( sumart(i[1],t) )
	for i in btoa:
		trenes_en_A.append( sumart(i[1],t) )

	for i in atob:
		j = buscarTren(trenes_en_A,i[0])
		if j == None:
			trenesA = trenesA + 1
		# else:
			# print "para el tren de las ",i[0],"desde A hasta B se usa el que llega de desde B a las", j
				# 
	for i in btoa:
		j = buscarTren(trenes_en_B,i[0])
		if j == None:
			trenesB = trenesB + 1
		# else:
			# print "para el tren de las ",i[0],"desde B hasta A se usa el que llega de desde A a las", j
			# 
	# print "a->b",atob
	# print "b->a",btoa
	# print
	# print trenes_en_A
	# print trenes_en_B
	return (trenesA,trenesB)
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	N = int(f.readline())
	
	for c in range(N):
		t = int(f.readline())
		na,nb = f.readline().strip(' \n\r').split(' ')
		na = int(na)
		nb = int(nb)
		
		atob = []
		for i in range(na):
			s,e = f.readline().strip(' \n\r').split(' ')
			
			sh = tuple( map(lambda f: int(f),s.split(':')) )
			eh = tuple( map(lambda f: int(f),e.split(':')) )
			atob.append([sh,eh])
		btoa = []
		for i in range(nb):
			s,e = f.readline().strip(' \n\r').split(' ')
			sh = tuple( map(lambda f: int(f),s.split(':')) )
			eh = tuple( map(lambda f: int(f),e.split(':')) )
			btoa.append([sh,eh])
		
		x = tren(t,atob,btoa)
		print "Case #%d: %d %d" % (c+1, x[0],x[1] )
		# print 
		# print
		i = i + 1
	f.close()
