import sys 

def ordenado(numero):
	for x in range(len(numero)-1,0,-1):
		if(numero[x]<numero[x-1]):
			numero[x-1]=str(int(numero[x-1])-1)
			for i in range(x,len(numero)):
				numero[i]='9'
	result=""
	for y in numero:
		result+=y
	return int(result)



casos=int(sys.stdin.readline().strip())

for x in range(0,casos):
	numero=list(sys.stdin.readline().strip())
	result=ordenado(numero)
	print("Case #"+str(x+1)+": "+str(result))
