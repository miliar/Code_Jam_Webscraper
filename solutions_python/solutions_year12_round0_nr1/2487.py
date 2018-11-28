ins="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

outs="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

trans=dict()
for i in range(len(ins)):
    trans[ins[i]]=outs[i]
trans['q']='z'
trans['z']='q'

entrada=open('/Users/yo/Downloads/A-small-attempt0.in')
salida=open('a.out','w')

n=int(entrada.readline())

i=0
for linea in entrada.readlines():
    i+=1
    salida.write('Case #'+str(i)+': ')
    modificada=""
    for char in linea:
        modificada+=trans[char]
    salida.write(modificada)
salida.close()
