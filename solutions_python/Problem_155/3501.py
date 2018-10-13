from sys import stdin

def main():
    casos=int(stdin.readline().strip())
    cont=0
    while(cont<casos):
        num=stdin.readline().strip().split()
        ans=[int(i) for i in num[1]]
        contador=0
        res=0
        for i in range(len(ans)):
            if i-1>=0 and contador < i and ans[i]>0:
                res+=(i-contador)
                contador+=res
            contador+=ans[i]
        cont+=1
        print("Case #{0}: {1}".format(cont,res))
main()
