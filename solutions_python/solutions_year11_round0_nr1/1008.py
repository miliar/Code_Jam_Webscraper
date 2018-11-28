class Robot:
	def __init__(self):
		self.pos = 1
		
###################################################

def numocero(num):
	if num > 0:
		return num
	else:
		return 0


fin = open('./Descargas/A-large.in','r')
fout = open('./A.out','w')
t = int(fin.readline())
i0 = 0
while i0 < t:
	o = Robot()
	b = Robot()
	ps = fin.readline().split()
	n = int(ps[0])
	to = 0
	tb = 0
	tt = 0
	i1 = 0
	while i1 < n:
		s = 2 * i1
		pasillo = ps[s + 1]
		boton = int(ps[s + 2])
		if pasillo == "O":
			tt = tt + numocero(abs(o.pos - boton) - tb) + 1
			to = to + numocero(abs(o.pos - boton) - tb) + 1
			tb = 0
			o.pos = boton
		else:
			tt = tt + numocero(abs(b.pos - boton) - to) + 1
			tb = tb + numocero(abs(b.pos - boton) - to) + 1
			to = 0
			b.pos = boton
		i1 = i1 + 1
	fout.write("Case #" + str(i0 + 1) + ": " + str(tt) + "\n")
	i0 = i0 + 1
