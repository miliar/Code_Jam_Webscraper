'''
Cookie rate analysis:
If 2 is cookies per second, C is the cost of cookie farms, and
you gain F cookies per second per cookies farm.

If you are going to buy a cookie farm, it makes sense to
buy it immediately. So you can say that the time to get to
X is equal to the time it get to the optimal rate plus the 
time is takes to get X. 

R = 2+C*F
Every new step is going to be shorter until we hit the max.
'''
file_name = "B-large"
raw_input = open(file_name+".in","r").read().split("\n")
test_cases = int(raw_input[0])
test_length = 1
output = ""

from decimal import *
getcontext().prec = 13
for i in range(test_cases):
    input = raw_input[i*test_length+1:i*test_length+test_length+1]
    Cs, Fs, Xs = input[0].split(" ")
    C = Decimal(Cs)
    F = Decimal(Fs)
    X = Decimal(Xs)
    R = Decimal(2.0)
    #TTC = time to completion
    best_TTC = X/R
    farm_TTC = 0
    new_farm_TTC = C/R
    new_R = R+F
    while best_TTC>farm_TTC + new_farm_TTC + X/new_R:
        best_TTC = farm_TTC + new_farm_TTC + X/new_R
        farm_TTC+= new_farm_TTC
        new_farm_TTC = C/new_R
        new_R+=F
    output+= "Case #%s: %s\n" % (i+1,best_TTC)
f = open(file_name+".out", "w")
f.write(output)
