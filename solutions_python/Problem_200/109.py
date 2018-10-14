entrada = open("B-large.in")
salida = open("b-out.txt",'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    n = [int(x) for x in entrada.readline().strip()]
    for d in xrange(-1,-len(n),-1):
        if n[d] < n[d-1]:
            n[d-1] = n[d-1]-1
            n[d::] = [9]*abs(d)
    while n[0] == 0:
        n.pop(0)
    salida.write("".join([str(x) for x in n])+"\n")