from math import *

def non_decreasing(N):
    digits = [int(d) for d in str(N)]
    try:
        return digits.index(0)-1
    except:
        pass
    for i in range(len(digits)-1):
        if digits[i]>digits[i+1]:
            return i
    return -1

f = open("C:\Python34\cjq2_sol.txt","w")
f.close()

with open("C:\Python34\cjq2.txt","r") as f:
    for i,line in enumerate(f.readlines()):
        N = int(line)
        if i>0:
            while (non_decreasing(N) != -1):
                ind = non_decreasing(N)
                digs = 1+floor(log10(N))
                digits = [9 if i>ind else int(d) for i,d in enumerate(str(N))]
                digits[ind] = digits[ind]-1
                N = int("".join([str(x) for x in digits]))
            with open("C:\Python34\cjq2_sol.txt","a") as f:
                f.write("Case #{}: {}\n".format(i, N))

