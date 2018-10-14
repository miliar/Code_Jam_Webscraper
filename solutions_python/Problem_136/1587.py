import sys
def menor(a,b):
    if a < b:
        return a
    else:
        return b

def calcular(C,F,X):
    Gini=2.0
    resp = X/float(Gini)
    tc= 0.0
    for itera in range(1,1000000):
        tc = tc + (C/float(Gini))
        Gini = Gini + F
        resp= menor(resp,(tc + (X/float(Gini))))
    return resp

def main():
    band = 0
    for line in sys.stdin:
        band = band + 1
        if band != 1:
            caso = band - 1
            param = (line.strip()).split()
            sol = calcular(float(param[0]),float(param[1]),float(param[2]))
            print (("Case #%i: %.7f")% (caso,sol))

main()