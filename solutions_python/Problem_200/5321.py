import numpy as numpy
def issorted(x):
    return (numpy.diff(x) >= 0).all()
def checkAndPrint(num,j):
    lst = [int(i) for i in str(num)]
    while len(lst)>=1:
        if issorted(numpy.array(lst)):
            print("Case #{}: {}".format(j,num ))
            break
        else:
            num=num-1
            lst = [int(i) for i in str(num)]

    
        
    

 # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
  number = input()  # read a list of integers, 2 in this case
  checkAndPrint(number,j) 
  
  # check out .format's specification for more formatting options
 
