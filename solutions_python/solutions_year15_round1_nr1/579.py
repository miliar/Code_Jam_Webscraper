def metodo1(linea):
    res = 0
    for i in range(len(linea)-1):
        posactual = linea[i]
        possig = linea[i+1]
        if(posactual>=possig):
            res+=posactual-possig
    return res

def metodo2(linea):
    maximo = -1
    res = 0
    for i in range(len(linea)-1):
        maximo=max(maximo,linea[i]-linea[i+1])
    for i in range(len(linea)-1):
        if(maximo>=linea[i]):
            res+=linea[i]
        else:
            res+=maximo
    return res
def main():
    casos = int(input())
    for i in range(casos):
        input()
        linea = [int(x) for x in input().strip().split()]
        print("Case #"+str(i+1)+":",metodo1(linea),metodo2(linea))
main()
