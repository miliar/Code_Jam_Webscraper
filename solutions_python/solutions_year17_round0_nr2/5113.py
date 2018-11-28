#!/usr/bin/env python3
output = []

def tidy(number):
    state = all(str(number)[i] <= str(number)[i+1] for i in range(len(str(number))-1))
    if state:
        return True,number
    else:
        return tidy(int(number)-1)

with open("B-small-attempt3.in","r") as File:
    lines = File.readlines()

i=0
t = int(lines[0])
while i<t:
    output.append("Case #{}: {}\n".format(i+1,tidy(int(lines[i+1]))[1]))
    i+=1

with open("tidyoutput.txt","w") as f:
    for i in output:
        f.write(i)
