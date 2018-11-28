from sys import stdin
dic = {}
dic["-"] = "+"
dic["+"] = "-"

def solution(m,y,n):
    cont = 0
    for i in range(len(m)):
        if m[i] == "-":
            if i+y <= len(m):
                for j in range(i,i+y):
                    m[j] = dic[m[j]]
                cont += 1
            else:
                print("Case #"+str(n+1)+": IMPOSSIBLE")
                return
    print("Case #"+str(n+1)+":",cont)
    return
    

def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(stdin.readline().split())
        p = list(m[0])
        y = int(m[1])
        conta = 0
        t = True
        if "-" not in p:
            print("Case #"+str(i+1)+":",0)
            continue
        else:
            solution(p,y,i)
            
        

main()
        
