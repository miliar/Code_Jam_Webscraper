import math
def toilet(start,end,people):
    if end - start <= 1:
        return (0,0)
    if people == 0:
        return (0,0)
    if people == 1:
        mid = (start+end)//2
        l = math.ceil((end - start)/2) - 1
        r = math.floor((end - start)/2) - 1
        return (l,r)
    else :
        mid = (start+end)//2
        np1 = (people-1)//2
        np2 = people - np1 -1 
        if (np2>np1):
            return toilet(mid,end,np2)
        else:
            return toilet(start,mid,np1)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  (r,l) = toilet(0,n+1,m)
  print("Case #{}: {} {}".format(i, r, l))
  # check out .format's specification for more formatting options
       