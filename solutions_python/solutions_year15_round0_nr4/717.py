f = open("D-small-attempt1.in")
salida = open("salida.txt", 'w')
casos = int(f.readline())
def resolver(X, R, C):
    if (R*C) % X != 0:
        return "RICHARD"
    if X >= 7:
        return "RICHARD"
    if ((R*C - X) <= X) and (X >= 4):
        return "RICHARD"
    if ((X-1)/2 > (R-1)) or ((X-1)/2 > (C-1)):
        return "RICHARD"
    return "GABRIEL"
for caso in range(1, casos+1):
    valores = f.readline().strip().split(" ")
    X = int(valores[0])
    R = int(valores[1])
    C = int(valores[2])
    salida.write("Case #"+str(caso)+": " + resolver(X,R,C) + '\n')
    print caso
    print valores
    print resolver(X, R, C)
salida.close()
