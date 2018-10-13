#!/usr/bin/python

in_file = "A-large.in"
out_file = "A-large.out"

try:
    f_in = open(in_file)
except IOError:
    print in_file, "can not be opened, plz check it out!"
    
try:
    f_out = open(out_file,"w+")
except IOError:
    print out_file, "can not be opened, plz check it out!"

N = int(f_in.readline())

for i in range(0,N):
    num = int(f_in.readline())
    x = f_in.readline().split()
    y = f_in.readline().split()
    for j in range(0,num):
        x[j] = int(x[j])
        y[j] = int(y[j])
    x.sort()
    y.sort()
    sum = 0
    for j in range(0,num):
        sum += x[j]*y[num-j-1]
#    print sum
    f_out.write("Case #" + str(i+1) + ": " + str(sum) + "\n")
    
f_in.close()
f_out.close()