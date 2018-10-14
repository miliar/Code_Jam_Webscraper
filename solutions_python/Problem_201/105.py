def resolver(n, k):
    if k == 1:
        return (n/2,n/2 -1 + n%2)
    k -= 1
    return resolver(n/2 + (k%2 - 1) * (1 - n%2), k/2 + k%2)

entrada = open("C-large.in")
salida = open("c-out.txt", 'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    y, z = resolver(*map(int, entrada.readline().strip().split()))
    salida.write(str(y)+" " +str(z) +"\n")