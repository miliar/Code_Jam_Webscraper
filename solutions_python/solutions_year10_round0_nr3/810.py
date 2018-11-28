import sys
from collections import deque

def do(R,k,N,grupos):
	d = deque()
	for i in grupos:
		d.append(int(i))
	
	print d
	salida=deque()
	dinero =0
	for i in range(0,R):
		restantes = k
		d.extend(salida)
		salida.clear()
		while (len(d)>0 and d[0]<=restantes):
			g=d.popleft()
			restantes-=g
			dinero+=g
			salida.append(g)
	return "%d" % dinero
		
    
print sys.argv
if len(sys.argv)<2:
    print "Faltan parametros"
    exit()


f = open(sys.argv[1],'r')
fileout = sys.argv[1][:-2]+"out"

o = open(fileout,'w')
ncasos = int(f.readline())

for i in range(1,ncasos+1):
	
	#elems=int(f.readline())
	
	cantidades=f.readline().rstrip()
	cantidades=cantidades.split(" ")
	
	R = int(cantidades[0])
	k = int(cantidades[1])
	N = int(cantidades[2])
	
	grupos = f.readline().rstrip().split(" ")
	
	resultado = do(R,k,N,grupos)
	print resultado
	
	o.write("Case #%d: "%i)
	o.write(resultado)
	o.write('\n')

f.close()
o.close()
raw_input("done")

