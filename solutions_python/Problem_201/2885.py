def function1(nstalls, npeople):
    stalls = [nstalls]
    # if npeople == nstalls or npeople == nstalls - 1:
    if npeople == nstalls:
        return [0, 0]
    else:
        while npeople > 0:
            stalls.sort()
            npeople -= 1
            if stalls[-1] % 2 == 1:
                temp1 = (stalls[-1] - 1) // 2
                temp2 = temp1
                stalls[-1] = temp1
                stalls.append(temp2)
            else:
                temp1 = stalls[-1] // 2
                temp2 = stalls[-1] // 2 - 1
                stalls[-1] = temp2
                stalls.append(temp1)
        return [stalls[-1], stalls[-2]]

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    templist = function1(n, m)
    print("Case #{}: {} {}".format(i, templist[0], templist[1]))
