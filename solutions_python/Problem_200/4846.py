def checkNumber(l):
    listA = []
    listB = []
    for i in range(l,0,-1):
        listA = list(str(i))
        listB = sorted(listA)
        if listA == listB:
            return i


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
n = int(input())  # read a line with a single integer
listB = []
for i in range(n):
    listB.append(int(input()))

for i in range(n):
        number = checkNumber(listB[i])
        print("Case #{}: {}".format(i+1,number))

