DEBUG = True
# DEBUG = False


def debug(show):
    if DEBUG is True:
        print(show)


def flip(pancakes, start, k):
    for i in range(k):
        if pancakes[start+i] is False:
            pancakes[start+i] = True
        else:
            pancakes[start+i] = False


def check(pancakes):
    for i in pancakes:
        if(i is False):
            return False
    return True


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems
t = int(input())  # read a line with a single integer


for i in range(1, t + 1):
    # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    line = input()
    s, k = line.split(" ")
    # debug(len(s))
    size = len(s)
    k = int(k)
    # (k)
    pancakes = []
    for p in s:
        if p is "+":
            pancakes.append(True)
        if p is "-":
            pancakes.append(False)
    count = 0
    for j in range(size-k+1):
        if(pancakes[j] is True):
            pass
        else:
            count += 1
            flip(pancakes, j, k)
    if(check(pancakes)):
        print("Case #{}:".format(i),count)
    else:
        print("Case #{}:".format(i),"IMPOSSIBLE")
    # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
