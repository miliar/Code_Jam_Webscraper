entrada = open("B-small-attempt1.in") 
salida = open("b.out", 'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #" + str(case) + ": ")
    n, rojo, nar, am, ver, az, vio = map(int, entrada.readline().split())
    if nar > az or vio > am or ver > rojo:
        salida.write("IMPOSSIBLE\n")
        continue
    if int(nar == az and nar > 0) + int(vio == am and vio > 0) + int(ver == rojo and ver > 0) > 1:
        salida.write("IMPOSSIBLE\n")
        continue
    elif (int(nar == az and nar > 0) + int(vio == am and vio > 0) + int(ver == rojo and ver > 0)) == 1:
        if nar == az and nar > 0:
            salida.write("OB"*nar)
        elif vio == am and vio > 0:
            salida.write("VY"*vio)
        else :
            salida.write("GR"*rojo)
        salida.write("\n")
        continue
    
    rojo -= ver
    az -= nar
    am -= vio
    colores = [rojo,az,am]
    maximo = max(colores)
    if maximo > sum(colores) - maximo:
        salida.write("IMPOSSIBLE\n")
        continue
    colores = [[rojo, "R"], [az, "B"], [am, "Y"]]
    colores.sort()
    res = ""
    while colores[2][0] != 0:
        c1 = colores[2][1]
        colores[2][0] -= 1
        if colores[1][0] > colores[0][0]:
            c2 = colores[1][1]
            colores[1][0] -= 1
        else :
            c2 = colores[0][1]
            colores[0][0] -= 1
        res += c1 + c2
    if c2 == colores[0][1]:
        res += (colores[1][1] + colores[0][1])*colores[0][0]
        if colores[1][0] > colores[0][0]:
            res += colores[1][1]
    else :
        res += (colores[0][1] + colores[1][1])*colores[1][0]
        if colores[0][0] > colores[1][0]:
            res += colores[0][1]
    if nar:
        i = res.index("B")
        res = res[:i] + "BO"*nar + res[i:]
    if ver:
        i = res.index("R")
        res = res[:i] + "RG"*ver + res[i:]
    if vio:
        i = res.index("Y")
        res = res[:i] + "YV"*vio + res[i:]
    if res[0] == res[-1]:
        print "uh"
    for i in xrange(n-1):
        if res[i] == res[i+1]:
            print n, rojo, nar, am, ver, az, vio, colores
    if res[0] == res[-1]:
        print "asdasd"
    salida.write(res+"\n")    