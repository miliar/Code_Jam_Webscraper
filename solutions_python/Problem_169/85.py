from fractions import Fraction as Frac

def do():
    times = eval(input())
    for i in range(1,times+1):
        print('Case #%d:'%i,end=" ")
        calculate()

def rate_sum(L):
    temp = sum((I[0]*I[1] for I in L),Frac())
    volu = sum((I[0] for I in L),Frac())
    return volu,temp/volu

def calculate():
    n,V,X = input().split()
    n,V,X = int(n),Frac(V),Frac(X)

    L = [input().split() for i in range(n)]
    L = [(Frac(l[0]),Frac(l[1])) for l in L]

    up,down,same = [],[],[]

    for I in L:
        if I[1] > X:
            up.append(I)
        elif I[1] == X:
            same.append(I)
        else:
            down.append(I)

    if len(up)+len(same) == 0 or len(same)+len(down) == 0:
        print("IMPOSSIBLE")
        return

    elif len(up) == 0 or len(down) == 0:
        result = V/sum((I[0] for I in same),Frac())

    else:
        UP = rate_sum(up)
        DOWN = rate_sum(down)
        SAME = sum((I[0] for I in same),Frac()),X

        upr = (X-DOWN[1])/UP[0]
        dor = (UP[1]-X)/DOWN[0]
        cur = max(upr,dor)

        result = cur*V/(UP[0]*upr+DOWN[0]*dor+SAME[0]*cur)

    print("%.7f"%float(result))



if __name__ == '__main__':
    do()

