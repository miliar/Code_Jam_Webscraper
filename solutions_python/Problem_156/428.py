from math import *  

#infile = open("Btest.txt", "r")
infile = open("Blarge.txt", "r")
outfile = open("Blargeout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    diners = int(infile.readline().rstrip())
    pancakes = infile.readline().rstrip().split()
    pancakes = [int(i) for i in pancakes]
    pancakes = sorted(pancakes)
    pancakes = pancakes[::-1]
    solution=100000
    maxcakes = pancakes[0]
    #print (maxcakes)
    for i in range(1, maxcakes+1):
        time = 0
        for cake in pancakes:
            if cake>i:
                time+=ceil(cake/i)-1
        time+=i
        #print(i, time)
        if time<solution:
            solution=time
    
    outline = "Case #"+str(z)+": "+str(solution)+"\n"
    outfile.write(outline)
    
infile.close()
outfile.close()
