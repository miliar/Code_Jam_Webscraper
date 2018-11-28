def lastTidy(n):
    strN = str(n)
    last_c = strN[0]
    counter = 0
    for c in strN:
        if c < last_c:
            lenNines = len(strN) - counter
            next_n = (int(strN[0:counter]) - 1)*(10**(lenNines))  + int('9' * lenNines)
            return lastTidy(next_n)
        last_c = c
        counter +=1
    return n

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, lastTidy(n)))
    # check out .format's specification for more formatting options
