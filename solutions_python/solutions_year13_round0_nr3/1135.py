import sys
import math
dummy = input()
for i,line in enumerate(sys.stdin):
    res = 0
    start, end = tuple(line.split())
    for num in range(int(start),int(end)+1):
        if (str(num) == str(num)[::-1]) and math.sqrt(num) % 1 == 0 and (str(int(math.sqrt(num))) == str(int(math.sqrt(num)))[::-1]):
            res+=1;
    print ("Case #",i+1,": ",res,sep='')

