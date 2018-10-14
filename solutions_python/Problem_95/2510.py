import sys

def retorna_normal(string):
    palavra = " abcdefghijklmnopqrstuvwxyz"
    modifi =  " ynficwlbkuomxsevzpdrjgthaq"
    nova_string = ""
    for c in string:
        try:
            nova_string += palavra[modifi.index(c)]
        except:
            pass
    return nova_string

arq_in = open(sys.argv[1],'r')
arq_out = open(sys.argv[2],'w')
           



linhas = arq_in.readlines()

string = ""
for i in range(int(linhas.pop(0))):
    string += "Case #%d: "%(i+1)     + retorna_normal(linhas.pop(0))+"\n"

arq_out.write(string.strip())
