from decimal import Decimal
from math import floor


def find_farm_num(C,F,X):
    k = ((X*F)-(2*C))/(C*F)
    if Decimal(floor(k)) == k:
        return floor(k)-1
    else:
        return floor(k)

def t_func(t,C,F,X):
    res = X/(2+(t*F))
    for i in range(0,t):
        res+=C/(2+i*F)
    return res


r = open("input","r")
lines = r.readlines()

w = open("output","w")

T = int(lines[0])

for i in range(1,T+1):
    CFX = lines[i].strip().split(" ")
    C = Decimal(CFX[0])
    F = Decimal(CFX[1])
    X = Decimal(CFX[2])
    farm_number = find_farm_num(C,F,X)
    if farm_number < 1:
        w.write("Case #"+str(i)+": " + str(X/Decimal(2))+"\n")
    else:
        time_to_win = t_func(farm_number,C,F,X)
        w.write("Case #"+str(i)+": " + str(time_to_win) + "\n")

