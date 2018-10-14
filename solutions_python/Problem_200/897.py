def check(number):
    for i, j in enumerate(number):
        for y in number[i:]:
            if j <= y:
                pass
            else:
                return False
    return True


t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    n_list = list(n)

    if check(n_list):
        print "Case #{}: {}".format(i, str(n))
        continue

    while not check(n_list):
        for index, number in reversed(list(enumerate(n_list))):
            for j in n_list[index:]:
                if number > j:
                    n_list = "".join(n_list[:index]) + str(int(n_list[index]) - 1) + (len(n_list) - index - 1) * "9"
                    break

    print "Case #{}: {}".format(i, str(int((n_list))))