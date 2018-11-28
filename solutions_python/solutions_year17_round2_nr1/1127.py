#from utils import *
#from numpy import *
#from math import *

infile = open("A-large.in")
outfile = open("A-large-out.txt", "w")
def time(d, k, s):
    return (d-k)/s

t = int(infile.readline())
for case in range(1, t+1):
    d, n = infile.readline().split(" ")
    d = int(d)
    n = int(n)
    horses = []
    for i in range(n):
        k, s = infile.readline().split(" ")
        k = int(k)
        s = int(s)
        horses.append((k ,s))
    max_time = 0
    for h in horses:
        k, s = h
        _time = time(d, k ,s)
        if _time > max_time:
            max_time = _time

    result = d/max_time
    print("Case #{0}: {1}".format(case, result), file = outfile)
outfile.close()
print("done")


    
        

        
    

