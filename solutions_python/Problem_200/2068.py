inp = open("tidynum.in", 'r')
opt = open("tidynum.out", 'w')

T = None
l = []
for line in inp:
    if T is None:
        T = int(line)
    else:
        l.append(line[:-1])

# plan: start with N, go backwards until tidy number is found
# store number is a list so that it can be easily changed
# look at the digit farthest to the right. If it is lower than the digit to its left, make it and all the digits to its
#   right 9s and subtract one from the digit to its left
# when we subtract 1 from a digit, check if it is 0. if it is, make it 9 and subtract 1 from digit to the left.

def subtract(lis, i):
    if lis[i] == "0":
        lis[i] = "9"
        return subtract(lis, i-1)
    lis[i] = str(int(lis[i])-1)
    return lis

for x in range(len(l)):
    num = list(l[x])
    i = len(num)-1
    while i > 0:
        if int(num[i]) < int(num[i-1]):
            for n in range(i, len(num)):
                num[n] = "9"
            num = subtract(num, i-1)
        i -= 1
    # remove leading 0s
    for y in range(len(num)):
        if num[y] == "0":
            num.pop(0)
        else:
            break
    s = ""
    for c in num:
        s += c
    opt.write("Case #" + str(x+1) + ": " + s + "\n")

opt.close()
