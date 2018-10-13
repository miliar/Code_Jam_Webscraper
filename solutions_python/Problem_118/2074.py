import math
f = open("DATA3.txt")
g = open("OUT3.txt",'w')
n = f.readline().strip()
for x in range(int(n)):
    i = f.readline().strip().split()
    y = int(0)
    while y*y < int(i[0]):
        y+=1
    print (y)
    counter =int(0)
    while int(y)*int(y) <= int(i[1]):
        if(str(int(y)*int(y)) == str(int(y)*int(y))[::-1]):
            if(str(y) == str(y)[::-1]):
                counter +=1
        y +=1
    g.write("Case #"+str(int(x+1))+": "+str(counter)+"\n")
g.close()
