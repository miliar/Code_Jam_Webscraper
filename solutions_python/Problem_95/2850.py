
f = open("A-small-attempt2.in")
a= int(f.readline())

cadenaMostrar=''
def translate(palabra):
    traduccion=''
    for v in range(len(palabra)):
        letra=palabra[v]
        if letra=='a':
            traduccion+="y"
        else:
            if letra=='b':
                traduccion+="h"
            else:
                if letra=='c':
                    traduccion+="e"
                else:
                    if letra=='d':
                        traduccion+="s"
                    else:
                        if letra=='e':
                            traduccion+="o"
                        else:
                            if letra=='f':
                                traduccion+="c"
                            else:
                                if letra=='g':
                                    traduccion+="v"
                                else:
                                    if letra=='h':
                                        traduccion+="x"
                                    else:
                                        if letra=='i':
                                            traduccion+="d"
                                        else:
                                            if letra=='j':
                                                traduccion+="u"
                                            else:
                                                if letra=='k':
                                                    traduccion+="i"
                                                else:
                                                    if letra=='l':
                                                        traduccion+="g"
                                                    else:
                                                        if letra=='m':
                                                            traduccion+="l"
                                                        else:
                                                            if letra=='n':
                                                                traduccion+="b"
                                                            else:
                                                                if letra=='o':
                                                                    traduccion+="k"
                                                                else:
                                                                    if letra=='p':
                                                                        traduccion+="r"
                                                                    else:
                                                                        if letra=='q':
                                                                            traduccion+="z"
                                                                        else:
                                                                            if letra=='r':
                                                                                traduccion+="t"
                                                                            else:
                                                                                if letra=='s':
                                                                                    traduccion+="n"
                                                                                else:
                                                                                    if letra=='t':
                                                                                        traduccion+="w"
                                                                                    else:
                                                                                        if letra=='u':
                                                                                            traduccion+="j"
                                                                                        else:
                                                                                            if letra=='v':
                                                                                                traduccion+="p"
                                                                                            else:
                                                                                                if letra=='w':
                                                                                                    traduccion+="f"
                                                                                                else:
                                                                                                    if letra=='x':
                                                                                                        traduccion+="m"
                                                                                                    else:
                                                                                                        if letra=='y':
                                                                                                            traduccion+="a"
                                                                                                        else:
                                                                                                            if letra=='z':
                                                                                                                traduccion+="q"
    return traduccion
    
    
for i in range(a):
    cadenaLinea = f.readline().strip()
    cadenaMostrar+="Case #" + str(i+1) + ":"
    import string
    listaPalabras=string.split(cadenaLinea, ' ', 100)
    for c in range(len(listaPalabras)):
        cadenaMostrar+=" "+ translate(listaPalabras[c])
    cadenaMostrar+='\n'
f.close()
print cadenaMostrar
    