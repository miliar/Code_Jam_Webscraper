# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 22-04-2017

def makeCircle(R, O, Y, G, B, V):
    key = []
    elements = []

    if R >= Y and R >= B:
        elements.append(R)
        key.append("R")
        if Y >= B:
            elements.append(Y)
            key.append("Y")
            elements.append(B)
            key.append("B")
        else:
            elements.append(B)
            key.append("B")
            elements.append(Y)
            key.append("Y")

    elif Y >= B and Y >= R:
        elements.append(Y)
        key.append("Y")
        if R >= B:
            elements.append(R)
            key.append("R")
            elements.append(B)
            key.append("B")
        else:
            elements.append(B)
            key.append("B")
            elements.append(R)
            key.append("R")
    else:
        elements.append(B)
        key.append("B")
        if R >= Y:
            elements.append(R)
            key.append("R")
            elements.append(Y)
            key.append("Y")
        else:
            elements.append(Y)
            key.append("Y")
            elements.append(R)
            key.append("R")

    result = ""
    if elements[0]>elements[1]+elements[2]:
        return "IMPOSSIBLE"
    else:
        while(elements[0]>0):
            result += key[0]
            elements[0] -= 1
            if elements[1]>elements[2]:
                result += key[1]
                elements[1] -= 1
            else:
                result += key[2]
                elements[2] -= 1
        while(sum(elements)>1):
            if elements[1]>elements[2]:
                result += key[1]
                elements[1] -= 1
                result += key[2]
                elements[2] -= 1
            else:
                result += key[2]
                elements[2] -= 1
                result += key[1]
                elements[1] -= 1
        for k,v in enumerate(elements):
            if v>0:
                result+=key[k]

    return result

T = int(raw_input())
for i in range(1, T + 1):
    N, R, O, Y, G, B, V = [int (e) for e in raw_input().split(" ")]

    result = makeCircle(R, O, Y, G, B, V)
    print("Case #{}: {}".format(i, result))
