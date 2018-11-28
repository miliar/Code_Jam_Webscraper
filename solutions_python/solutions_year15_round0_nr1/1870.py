#a es el numero de casos a evaluar
a=input()

#Transformamos a a entero
a=int(a)

#inicializamos el contador para el numero de casos
i=0
while i!= a:
	
	#b es el string que contiene el numero maximo de timidez 
	b=input()
	
	#Lo separamos en dos campos
	b=b.split(' ')
	
	#Definimos la timidez
	timidez=int(b[0])
	
	#Definimos las personas
	personas=b[1]
	
	#Vemos el primer elemento del arreglo para saber cuantos hay de pie
	parados=int(personas[0])
	
	#En r almacenamos cuantos amigos hay que invitar
	r=0
	
	#Mientras no se alcanza el nivel maximo de timidez y j no se sale de rango, hacemos:
	j=1
	while j<len(personas) and parados<timidez:
		
		#En cada posicion, si el numero de parados es menor a la timidez entonces sumamos un amigo y agregamos un parado
		while parados<j:
			parados=parados + 1
			r=r+1
		
		#En este punto el numero de parados es igual a la timidez, por lo cual todos los de la posicion se levantan
		parados=parados+int(personas[j])
		j=j+1
	
	i=i+1
	
	#Imprimimos
	print('Case #'+str(i)+': '+str(r))
