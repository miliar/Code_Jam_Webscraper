
string1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

string2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

diccionario = {}
tam = len(string1)
for i in range(0,tam):
  if string1[i]=='z':
    print "espacio"
  else:
    diccionario[string1[i]]=string2[i]

diccionario["z"]='q'
diccionario['q']='z'

file	= open("A-small-attempt1.in")
output  = open("Output.in","w")
linea	= file.readline()
print linea.split("\n")
num_cases	=int( linea.split("\n")[0])
cumple  = False
credit = 0
tam     = 0
for i in range(0,num_cases):
	traduccion = ""
	linea  = file.readline()
	for x in linea:
	  if x!='\n':
	    traduccion = traduccion + diccionario[x]
	print traduccion
	output.write("Case #"+str(i+1)+": "+traduccion+"\n")
file.close()
output.close()
  
