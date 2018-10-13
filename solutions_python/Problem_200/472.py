def get_digits_from_number(number):
    lst = []
    while number:
        lst.append(number % 10)
        number /= 10
    return list(reversed(lst))

def check_number(number):
    lst = get_digits_from_number(number)
    flag = True
    for i in xrange(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            flag = False
            break

    return flag

def get_number_from_list(lst):
    val = 0
    for item in lst:
        val *= 10
        val += item

    return val

def get_number(number):
    lst = get_digits_from_number(number)

    bp = -1
    last = 0
    for i in xrange(len(lst) - 1):
        if i > 0:
            if lst[i] != lst[i - 1]:
                last = i

        if lst[i] > lst[i + 1]:
            bp = last
            break

    if bp != -1:
        if lst[bp] != 0:
            t = lst[:bp]
            t += [lst[bp] - 1]
            t += [9 for _ in xrange(len(lst) - bp - 1)]
            lst = t
        else:
            lst = lst[:bp - 1] + [lst[bp] - 1] + [9 for _ in xrange(len(lst) - bp)]

    return lst

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, get_number_from_list(get_number(n)))
#
# last = 0
# for i in xrange(1109, 100990):
#     if check_number(i): last = i
#
#     t = get_number(i)
#     g = get_number_from_list(t)
#     if g != last:
#         print i, get_number(i), get_digits_from_number(last)