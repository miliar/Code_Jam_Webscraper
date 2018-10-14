def main():
    count=1
    cont=int(input())
    for i in range(cont):
        lista=[]
        numero=input()
        for i in numero:
            lista.append(int(i))
        while True:
            if lista==sorted(lista):
                break
            else:
                numero=str(int(numero)-1)
                lista=[]
                for i in numero:
                    lista.append(int(i))
                    
        print("Case #{}:".format(count),int(numero))
        count+=1
main()
