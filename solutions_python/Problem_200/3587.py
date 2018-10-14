def print_tidy(number):
    d_list = map(lambda x: int(x), number)

    for j in xrange(len(d_list) - 1, 0, -1):
        if d_list[j] < d_list[j - 1]:
            for k in xrange(j, len(d_list)):
                d_list[k] = 9
            d_list[j - 1] -= 1
    try:
        d_list.remove(0)
    except:
        pass

    output = "".join(str(n) for n in d_list)
    return output

t = int(raw_input())
for i in xrange(1, t + 1):
    number = raw_input()

    print "Case #%d: %s" % (i, print_tidy(number=number))


