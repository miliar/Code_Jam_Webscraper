import math
input_file = "D-small-attempt2.in"


def line(f,_type=str):
    s = [_type(i) for i in f.readline().strip().split()]
    return s

def f(x,r,c):
    #True = Richard. False = Gabriel
    r,c = max(r,c), min(r,c)
    if r*c % x != 0:
        return True
    if r < x and c < x:
        return True
    if x == 1:
        return False
    if x == 2:
        return False
    if x == 3 and c <= 1:
        return True
    if x == 4 and c <= 2:
        return True
    if x == 5 and c <= 3:
        return True
    if x == 6 and c <= 3:
        return True
    if x >= 7:
        return True
    return False
    
    

with open(input_file) as fin:
    with open('output.txt','w') as fout:
        T = line(fin,int)[0]
        for case in range(1,T+1):
            x,r,c = line(fin,int)
            if f(x,r,c):
                fout.write("Case #%d: RICHARD\n" % case)
            else:
                fout.write("Case #%d: GABRIEL\n" % case)
