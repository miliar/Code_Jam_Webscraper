'''
Created on 13/04/2012

@author: harold
'''

dict = {'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q',
' ':' ',
'\n':''}

archivo = open('A-small-attempt0.bin')
lista = archivo.readlines()
limite = lista.pop(0)

def traducir(frase):
    respuesta = ''
    for letra in frase:
        respuesta += dict[letra]
    return respuesta

respuesta = [traducir(x) for x in lista]
out = open('archivo.out', 'w')
contador = 1
for linea in respuesta[0:int(limite)]:
    out.write('Case #%i: %s\n' % (contador, linea))
    contador += 1


