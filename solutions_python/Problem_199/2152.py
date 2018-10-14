from sys import stdin
dic = {}
dic["-"] = "+"
dic["+"] = "-"

def solution(linea,k,n):
    cont = 0
    for i in range(len(linea)):
        if linea[i] == "-":
            if i+k <= len(linea):
                for j in range(i,i+k):
                    linea[j] = dic[linea[j]]
                cont += 1
            else:
                print("Case #"+str(n+1)+": IMPOSSIBLE")
                return
    print("Case #"+str(n+1)+":",cont)
    return
    

def main():
    n = int(stdin.readline())
    for i in range(n):
        linea = list(stdin.readline().split())
        dato = list(linea[0])
        k = int(linea[1])
        if "-" not in dato:
            print("Case #"+str(i+1)+":",0)
            continue
        else:
            solution(dato,k,i)
            
        

main()
        
