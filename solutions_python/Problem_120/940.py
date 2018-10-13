import math


myfile = open("A-small-attempt0.in.txt", "r")
output = open("output.txt", "w")

cases = int(myfile.readline())

for case in range(cases):
    (radius, paint) = map(int, myfile.readline().split())
    middle = radius +0.5 
    count = 0 
    while paint>0:
        needpaint = middle*2
        #print needpaint, case
        paint = paint -needpaint
        #print paint
        if paint>=0:
            count +=1
        middle = middle + 2
    
    out = "Case #%d: " %(case+1) + str(count)
    output.write(out+"\n")

myfile.close()
output.close()
