import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print("Case #" + str(i) + ":", end=' ')
    
    # read test case
    tmp = f.readline().split()
    a = int(tmp[0])
    b = int(tmp[1])
    k = int(tmp[2])

    catalina = 0
    for i in range(a):
        for j in range(b):
            if (i & j) < k:
                catalina += 1
    print(catalina)
