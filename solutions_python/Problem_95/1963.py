

diccionario = {"\n":'',"a":'y',"b":'h',"c":'e',"d":'s',"e":'o',"f":'c',"g":'v',"h":'x',"i":'d',"j":'u',"k":'i',"l":'g',"m":'l',"n":'b',"o":'k',"p":'r',"q":'z',"r":'t',"s":'n',"t":'w',"u":'j',"v":'p',"w":'f',"x":'m',"y":'a',"z":'q'," ":' '}

f = open("examen", "r")
linea = f.readline()
for i in range(int(linea)):
   output=""
   cad = f.readline()
   for e in cad:
      output+=diccionario[e]
   print "Case #"+str(i+1)+": "+ output

