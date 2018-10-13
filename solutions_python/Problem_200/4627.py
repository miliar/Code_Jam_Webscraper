def checksort(num):
    num2 = num
    while num2 > 0:
        numlist = list(str(num2))
        if all(numlist[i] <= numlist[i+1] for i in range(len(numlist)-1)):
            return ''.join(numlist)
        else:
            num2 -= 1

# print(checksort(1))
# print(checksort(10))
# print(checksort(21))
# print(checksort(32))
#print(checksort(111111111111111110))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    j = int(input())
    result = checksort(j)
    print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options
