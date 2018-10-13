def parseSign(sign):
    n = []
    for char in sign:
        if char == "+":
            n = n + [1]
        else:
            n = n + [0]
    return n


def flip_list(L,k):
    step = 0
    while (len(L) >= k):
        if L[0] == 1:
            L.remove(1)
        else :
            step += 1
            L.remove(0)
            for i2 in range(0,k-1):
                L[i2] = 1 - L[i2]
    if k == 1:
        return step
    else:
        for i2 in L:
            if i2 == 0:
                return -1
        return step

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [s for s in input().split(" ")]  
    # read a list of integers, 2 in this case
    L = parseSign(n)
    ret = flip_list(L,int(m))
    if ret == -1:
        retnum = "IMPOSSIBLE"
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i,ret))
    # check out .format's specification for more formatting options
 
