
a=input()
a=int(a)
i=1

while i<=a:
	b=input()
	b=b.split(' ')
	n=int(b[0])

	#Alto es el mayor de los lados
	alto=max(int(b[1]),int(b[2]))
	
	#Ancho es el menor de los lados
	ancho=min(int(b[1]),int(b[2]))
	
	#Conjunto de todos los espacios, el cuadrado completo
	espacio=alto*ancho
	
	#Si el n es  impar, entonces:

	if n==1:
		print('Case #'+str(i)+': GABRIEL')			
	elif n==2:
		if alto*ancho>=2 and alto*ancho%2==0:
			print('Case #'+str(i)+': GABRIEL')		
		else:
			print('Case #'+str(i)+': RICHARD')		
			
	elif n>2:
		if n%2==1:
			
			escaleraAl=(n//2)+1
			escaleraAn=escaleraAl
			inside=(escaleraAl*escaleraAn)-n
			insideDown=inside//2
			insideUp=inside-insideDown
			
		elif n%2==0:
			escaleraAl=(n//2)+1
			escaleraAn=(n//2)
			inside=((escaleraAl*escaleraAn)-n)
			insideDown=inside//2
			insideUp=insideDown
			
		escalera=min(escaleraAn,escaleraAl)
		quedaAn=(ancho-escaleraAn)
		quedaAl=(alto-escaleraAl)
		
		#if (quedaAl==0 or quedaAn==0) 
		restante=(insideUp+((quedaAl*ancho)+(quedaAn*alto)))
		if espacio%n!=0 or (escalera>ancho) :
			print('Case #'+str(i)+': RICHARD')
		elif quedaAl==0:
			if (insideDown+restante)%n==0 and restante%ancho==0:
				print('Case #'+str(i)+': GABRIEL')
			else:
				print('Case #'+str(i)+': RICHARD')			
		elif quedaAn==0:	
			if (insideDown+restante)%n==0 and restante%alto==0:
				print('Case #'+str(i)+': GABRIEL')
			else:
				print('Case #'+str(i)+': RICHARD')		
		#si el lado mas peque;o de la escalera es mas grande que los lados del espacio entonces falla
		elif quedaAn!=0 and quedaAl!=0 and espacio%n==0:
			print('Case #'+str(i)+': GABRIEL')		
		elif quedaAn!=0 and quedaAl!=0 and espacio%n!=0:
			print('Case #'+str(i)+': RICHARD')				
		elif espacio%n!=0 or (escalera>ancho or escalera>alto) :
			print('Case #'+str(i)+': RICHARD')
		else:
			print('Case #'+str(i)+': GABRIEL')

	else:
		print('Case #'+str(i)+': GABRIEL')		
	i=i+1