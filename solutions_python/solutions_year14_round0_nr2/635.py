from sys import argv
import math


#f = open("ex_B.in")
f = open("B-large.in")
cases = int(f.readline())

def cookie(C, F, X):
    #X = float(X);
    time = 0.0
    num_of_farm = ((X-C)/C)-2.0/F
    if num_of_farm > 0:
        num_of_farm = int(math.ceil(num_of_farm))
    else:
        num_of_farm = 0
    for i in range(num_of_farm + 1):
        time += C/(2.0 + i*F)
    time += (X-C)/(2.0 + num_of_farm*F)
    return time

for i in range(cases):
    C, F, X = map(float, f.readline().split())
    result = cookie(C, F, X)
    print "Case #%d:" %(i+1),result
