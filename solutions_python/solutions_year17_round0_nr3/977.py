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


def level(k):
    count = 0
    tmp = k
    while(tmp > 1):
        tmp = int(tmp/2)
        count += 1
    return count + 1


def devide_to_base(total, level):
    return int((total - (2**(level-1)-1))/(2**(level-1)))


def n_of_larger_base(total, level):
    result = total - devide_to_base(total, level)*(2**(level-1)) - 2**(level-1) + 1
    return result


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems
t = int(input())  # read a line with a single integer


for i in range(1, t + 1):
    # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    line = input()
    n, k = line.split(" ")
    n = int(n)
    k = int(k)
    # print(n, k)
    # print(level(8))
    ll = level(k)
    base = devide_to_base(n, ll)
    excess = k - (2**(ll-1)) + 1
    if(excess <= n_of_larger_base(n, ll)):
        this_one = base + 1
    else:
        this_one = base
    print("Case #{}: {} {}".format(i, int(this_one/2), int((this_one-1)/2)))
    # print(n_of_larger_base(102, 3))
    # print("Case #{}: {}".format(i, out))
    # print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
