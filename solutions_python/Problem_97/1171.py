#!/usr/bin/python
fichero = open("input",'r')
num = int(fichero.readline())

for i in range(num):
	case = "Case #"+str(i+1)+": "
	linea = fichero.readline()
	#empieza
	datos = linea.split(" ")
	a = int(datos[0])
	b = int(datos[1])
	
	n = a
	cont = 0


	while n < b:
	
		m = a + 1
		while m <= b:
			if n < m:
			
				for i in range(len(str(m))):
					m = str(m)[len(str(m))-1]+str(m)[:-1]
					if str(n) == m:
						
						cont = cont + 1
					
			
			m = int(m)
			m = m + 1


		n = n + 1
	print case+str(cont)

		
	
