def main():
    linea = int(input())
    for i in range(linea):
        line = input().strip().split()
        string = line[1]
        cant = 0
        funciona = True
        termino = False
        while(funciona==True and termino==False):
            aplaudiendo=cant
            for j in range(len(string)):
                pos_actual = string[j]
                if(aplaudiendo>=j):
                    aplaudiendo+=int(string[j])
                else:
                    funciona=False
                    break
            if(funciona==True):
                termino=True
            else:
                funciona=True
                termino=False
            cant+=1
        print("Case #"+str(i+1)+":",cant-1)
main()
