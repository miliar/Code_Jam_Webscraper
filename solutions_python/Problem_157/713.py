import time

matriz = [['1','i','j','k'],
          ['i','-1','k','-j'],
          ['j','-k','-1','i'],
          ['k','j','-i','-1']]

def multiplicar(i,j):
    stri = '1ijk'
    menos = 0
    if '-' in i:
        i = i[1:]
        menos += 1
    if '-' in j:
        j = j[1:]
        menos += 1
    resultado = matriz[stri.index(i)][stri.index(j)]
    if '-' in resultado:
        menos += 1
        resultado = resultado[1:]
    menos = menos % 2
    if menos:
        resultado = '-'+resultado
    return resultado

def generate(string,letter,number):
    try:

        if letter == 'k':
            while len(string) > 3:
                if string[number] == '-':

                    string = string[:number]+multiplicar(string[number:number+2],string[number+2])+string[number+3:]
                else:    
                    string = string[:number]+multiplicar(string[number],string[number+1])+string[number+2:]

        else:
            while string[number] != letter:

                if len(string) <= 3:
                    break
                
                if string[number] == '-':

                    string = string[:number]+multiplicar(string[number:number+2],string[number+2])+string[number+3:]
                else:    
                    string = string[:number]+multiplicar(string[number],string[number+1])+string[number+2:]

    except:
        pass
    return string


cases = int(input())

for i in range(cases):
    X,L = map(int,input().split())
    string = input()*L

    string = generate(string,'i',0)
    string = generate(string,'j',1)
    string = generate(string,'k',2)
    if string == 'ijk':
        resul = "YES"
    else:
        resul = "NO"
    print("Case #"+str(i+1)+":",resul)
