import math
import re
import time
import numpy

with open("A-large.in") as f:
    number_of_cases = int(f.readline())
    output = ""
    i = 1
    while i<number_of_cases+1:
        dimensions = f.readline()
        print("dim" + dimensions)
        D = int(re.split('\W+', dimensions)[0])
        N = int(re.split('\W+', dimensions)[1])
        
        tmax = 0

        for n in range(0,N):
            dimensions = f.readline()
            Di = int(re.split('\W+', dimensions)[0])
            Vi= int(re.split('\W+', dimensions)[1])
            t = (D - Di)/Vi
            tmax = max(tmax,t)
        v = D/tmax
        print("v:",v)
        output+="Case #"+str(i)+": "+str(v) + "\n"
        i +=1

print()
print()
print(output)
with open('Alargeoutput.in', 'w') as file:
    file.write(output)