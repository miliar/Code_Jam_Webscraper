#!/usr/bin/python
# intento de resolver el problema B de la ronda de clasificacion

#considero que todos los trenes salen cuando deben
#y despues busco por cada horario de A a B
#si hay algun horario de salida de B a A que sea menor que el horario de llegada de A a B
#si es asi resto 1 a la cantidad de trenes necesaria para B
#siendo la cantidad inicial la cantidad de viajes sin optimizacion



#**********************
# SECTOR DE FUNCIONES
#**********************



#
#convierte un string en formato HH:MM en un entero que representa los minutos pasados desde las 00:00
#

def date_convert(date_string):
	horas=int(date_string.split(':')[0])
	minutos=int(date_string.split(':')[1])
	return horas*60+minutos



#
# funcion principal
# toma dos listas de horarios en formato minutal (la primera de llegada y la segunda de partida)
# y devuelve cuantos trenes se ahorraron en la estacion gracias a los que venian
# tomando como dato que el tiempo que tarda en acomodarse un tren desde que llega a la estacion es T
#

def train_count(horarios_llegada, horarios_partida, T):
	ahorrados=0
	horarios_partida.sort()
	
	for i in horarios_llegada:
		for j in horarios_partida:
			#print "caso",i,j
			if( i+T <= j ):
				#print "como "+str(i)+' + '+str(T)+' <= '+str(j)+', voy a tomar ese horario con el tren que viene'
				horarios_partida.remove(j)
				#print horarios_partida
				ahorrados+=1
				break
				
	return ahorrados



#******************************
# SECTOR DE CODIGO DE PROGRAMA
#******************************



file=open('./B-large.in','r')
#you can change the name to get the input from other file
# I'm sorry for my bad programming, I'm new to python :D
#and comments are in english and spanish because I'm from argentina




N=file.readline().strip('\n')
#print N

acumulador_rta=''
for i in xrange(0,int(N)):
	#print "case %s" % (i)
	T=int(file.readline().strip('\n'))
	primera_linea=file.readline().strip('\n')
	NA=primera_linea.split(' ')[0]
	NB=primera_linea.split(' ')[1]
	#print T, NA, NB
	lista_salida_A=[]
	lista_arribos_B=[]
	for j in xrange(0,int(NA)):
		linea_leida=file.readline().strip('\n')
		lista_salida_A.append(date_convert(linea_leida.split(' ')[0]))
		lista_arribos_B.append(date_convert(linea_leida.split(' ')[1]))
	
	
	#print lista_salida_A, lista_arribos_B
	
		
	lista_arribos_A=[]
	lista_salida_B=[]
	for j in xrange(0,int(NB)):
		linea_leida=file.readline().strip('\n')
		lista_salida_B.append(date_convert(linea_leida.split(' ')[0]))
		lista_arribos_A.append(date_convert(linea_leida.split(' ')[1]))
		
	#print lista_salida_B, lista_arribos_A
		
	rtaB=int(NB)-train_count(lista_arribos_B,lista_salida_B,T)
	rtaA=int(NA)-train_count(lista_arribos_A,lista_salida_A,T)
	acumulador_rta=acumulador_rta +'Case #'+str(i+1)+': '+ str(rtaA) +' '+str(rtaB)+'\n'
	

file.close()

file_dest=open('./B-large.out','w')
file_dest.write(acumulador_rta)

file_dest.close()
		