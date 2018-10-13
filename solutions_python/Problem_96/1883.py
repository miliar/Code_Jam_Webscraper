file	= open("B-small-attempt7.in")
output  = open("Output.in","w")
linea	= file.readline()
print linea.split("\n")
num_cases	=int( linea.split("\n")[0])
cumple  = False
credit  = 0
tam     = 0
total   = 0
for j in range(0,num_cases):
	traduccion = ""
	linea  = file.readline()
	raw  = linea.split("\n")
	datos  = raw[0].split(" ")
	print datos
	googlers = int(datos[0])
	surprise = int(datos[1])
	#print "Surprise :" + str(surprise)
	p        = int(datos[2])
	total    = 0
	for i in range(3,len(datos)):
		#print "Numero" + str(datos[i]) + " --- "
		num  = int(datos[i])/3
		numero = int(datos[i])
		#print "Numero:"+ str(num) + " p:"+str(p)
		if p == 0 and numero >= 0:
			total = total + 1
			print "Caso Especial 1:" + str(j+1)+" con el numero : " + str(numero)
		elif p > 0 and p < 3 and numero < 3 and numero>=p:
			print "Caso Especial 2:" + str(j+1)+" con el numero : " + str(numero)
			total = total + 1
		elif p > 2 and numero<((p*3)-2) and numero>(p-2)*3  and surprise>0 and numero > 0:
  	#if abs(num-p)==2 and num<p and surprise>0 and (int(datos[i]) % p-2 )!=0 :
			surprise=surprise-1
			total = total + 1
		#elif num-p>-2 and num<p and int(datos[i]) > 0:
		elif numero>=((p*3)-2):	
			total = total + 1
		#	print "Entre"
	output.write("Case #"+str(j+1)+": "+str(total)+"\n")
file.close()
output.close()
