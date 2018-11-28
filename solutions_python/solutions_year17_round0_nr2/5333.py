
def numbers_increase(numb):
    for i in range(1, len(str(numb))):
        if int(str(numb)[i]) < int(str(numb)[i-1]):
            return False
    return True


def is_numb_tiny(numb):
    if 0 <= numb < 10:
        return True
    elif(numbers_increase(numb)):
        return True
    else:
        return False


def is_tiny(numb):
    found = -1
    #for i in xrange(numb):
    i = numb
    while i > 0:
        # new_num = numb - i
        if str(i).rfind('0') > 0:
            good = True
            for ll in range(str(i).rfind('0')):
                if int(str(i)[ll]) != 1:
                    good = False
            if good:
                exp = str(i).rfind('0')
                i = int(str(i)[0]) * pow(10, exp+1)
            pass
        elif(is_numb_tiny(i)):
            found = i
            i = -1
        i -= 1
    return found



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    m = [long(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    ans = is_tiny(m[0])

    print "Case #{}: {}".format(i, ans)
    # check out .format's specification for more formatting options