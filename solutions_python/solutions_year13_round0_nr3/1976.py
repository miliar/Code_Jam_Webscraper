from math import *
f = open('C-small-attempt0.in', 'r')
q = open('output', 'w')
x = f.readlines()


t = int(x[0])

counter = 1
field = []

for i in range(t):
    value = 0
    field.append(x[counter])
    field[0] = field[0].split()
    A = field[0][0]
    B = field[0][1]

    start = int(sqrt(float(A)))
    end = int(sqrt(float(B)))

    while start <= end:
        if  (start == int(str(start)[::-1])) and (start**2 == int(str(start**2)[::-1])) and start**2 >= int(A):
            value += 1
        start += 1
    
    
    q.write("Case #" + str(i+1) + ": " + str(value) + "\n")
    counter += 1
    field = []

f.close()
q.close()
print "Finished"
