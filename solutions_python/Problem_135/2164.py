__author__ = 'Narrenschyff'
from sets import Set
f = open("A-small-attempt0.in", "r")
o = open("outputA","w")
N = f.readline()
for i in range(1,int(N)+1):
    row =  int(f.readline())
    for j in range(1,5):
        line = f.readline()
        if(row == j):
            arr  = Set([int(t) for t in line.split()])
    row =  int(f.readline())
    for j in range(1,5):
        line = f.readline()
        if(row == j):
            arr2  = Set([int(t) for t in line.split()])

    arr = arr.intersection(arr2)

    if(len(arr) > 1):
        o.write(("Case #"+str(i)+": Bad magician!\n"))
    elif(len(arr) == 1):
        o.write(str(("Case #"+str(i)+": "+str(arr.pop()))+"\n"))
    elif(len(arr) == 0):
        o.write("Case #"+str(i)+": Volunteer cheated!\n")
o.close()
