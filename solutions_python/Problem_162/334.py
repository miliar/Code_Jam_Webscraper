f = open("A-small-attempt9.in")
salida = open("salida1.txt", 'w')
enes = {1:1}
def resolver(n):
    if n in enes:
        return enes[n]
    else:
        if int(str(n)[::-1]) < n and len(str(int(str(n)[::-1]))) == len(str(n)) :
            res = min(resolver(n-1)+1, resolver(int(str(n)[::-1]))+1)
            enes[n] = res
            return res
        else :
            res = resolver(n-1)+1
            enes[n] = res
            return res
for i in range(1, 1000000):
    resolver(i)

casos = f.readline()
caso = 0
for linea in f:
    caso += 1
    n = int(linea)
    k = 1
    total = 1
    while k < n:
        if int(str(k)[::-1]) == n:
            k = int(str(k)[::-1])
        elif k > 9 and len(str(k)) < len(str(n)) and str(k)[len(str(k))-1] != "9":
            k +=1
        elif len(str(k)) == len(str(n)):
            if int(str(k)[::-1]) <= n and (int(str(k+1)[::-1]) > n or str(k+1)[len(str(k+1))-1] == "0") and int(str(k)[::-1]) > k:
                k = int(str(k)[::-1])
            else :
                k += 1
        elif int(str(k)[::-1]) > k and int(str(k)[::-1]) <= n:
            k = int(str(k)[::-1])
        else :
            k += 1
        total += 1
#    if n < 900:
#        if total != resolver(n):
#            print n
#    print n, total
    salida.write("Case #" + str(caso) + ": " + str(resolver(n))+'\n')


salida.close()