from operator import and_
entrada = open("A-large.in")
salida = open("a-out.txt",'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    si, k = entrada.readline().split()
    k = int(k)
    s = [i == "+" for i in si]
    total = 0
    for i in xrange(len(s)-k+1):
        if not s[i]:
            for j in xrange(k):
                s[i+j] = not s[i+j]
            total += 1
    if not reduce(and_, s):
        salida.write("IMPOSSIBLE\n")
    else:
        salida.write(str(total)+"\n")