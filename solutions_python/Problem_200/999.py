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
    n = line
    pre = n[0]
    out = ""
    top = False
    tmp = 0
    for j in n[1:]:
        if top:
            out += "9"
        else:
            if(int(pre) < int(j)):
                out += (tmp+1)*pre
                tmp = 0
            if(int(pre) == int(j)):
                tmp += 1
            if(int(pre) > int(j)):
                if(int(pre) == 1):
                    out += tmp*"9"
                else:
                    out += str(int(pre)-1)
                    out += tmp*"9"
                top = True
        pre = j
    if top:
        out += "9"
    else:
        out += (tmp+1)*pre
    # debug(len(s))
    print("Case #{}: {}".format(i, out))
    # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
