import sys
from collections import deque

def do(n,k):
	snappers  = [0]*n
	idx=0
	while idx < k:
		#print snappers
		if snappers[0]==1:
			i=1
			while i<n:
				if snappers[i]==1:
					i+=1
					continue
				else:
					snappers[i] = 1-snappers[i]
					break
			j=i-1
			while j>=0:
				snappers[j]=0
				j-=1
		else:
			snappers[0]=1
				
				
		idx=idx+1
	idx2=0
	
	while idx2 < n:
		if snappers[idx2]==0:
			return "OFF"
		else:
			idx2=idx2+1
	return "ON"
		
	
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
	
	n = int(cantidades[0])
	k = int(cantidades[1])
	
	resultado = do(n,k)
	#print resultado
	
	o.write("Case #%d: "%i)
	o.write(resultado)
	o.write('\n')

f.close()
o.close()
raw_input("done")

