import math
filein = open('C-small-attempt0.in', mode='r')
fileout = open('C-small-attempt0.out', mode='w')
T = filein.readline()

for case in range(1, int(T)+1):
    size = filein.readline().strip().split(" ")
    A = int(size[0])
    B = int(size[1]) 
    a = math.floor(math.sqrt(A))
    b = math.ceil(math.sqrt(B))
    tally = 0
    for num in range(a, b + 1):
        if str(num) == (str(num)[::-1]):
            squared = num * num
            if (squared >= A and squared <= B and str(squared) == (str(squared) [::-1])):
                tally = tally + 1
    
    result = "Case #" + str(case) + ": " + str(tally) + "\n" 
    fileout.write(result)

filein.close()
fileout.close()
