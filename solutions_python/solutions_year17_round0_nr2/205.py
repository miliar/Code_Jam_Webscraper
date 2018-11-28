import sys

f = sys.stdin
cases = int(f.readline().strip())

# Get the index of where the next digit is less than this one
# EX: "1099" returns 0
# If str is tidy, return -1
def getTidyIndex(num):
    i = 0
    size = len(num)

    while(i < size-1):
        if(num[i+1] < num[i]):
            return i
        i += 1

    return -1


for ii in range(cases):
    rawnum = f.readline().strip()
    num = []
    for i in rawnum:
        num.append(int(i))

    size = len(num)

    ti = getTidyIndex(num)
    while(ti != -1):

        num[ti] -= 1
        for i in range(ti+1, size):
            num[i] = 9

        ti = getTidyIndex(num)

    # If we're here, we finished the number off

    ans = int("".join(str(x) for x in num))

    print ("Case #{0}: {1}".format(ii+1, ans))

