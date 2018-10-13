import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print("Case #" + str(i) + ":", end=' ')
    
    # read test case
    tc = f.readline().split(' ')
    smax = int(tc[0])
    
    # check test case for row
    stand = 0
    friend = 0
    for i in range(0, smax + 1):
        if stand < i:
            friend += (i - stand)
            stand = i
        stand += int(tc[1][i])
    print(friend)
