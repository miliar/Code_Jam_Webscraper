def isTidy(num):
    int_list = [int(s) for s in str(num)]
    current_num = int_list[0]

    for digit in int_list[1:]:
        if current_num <= digit:
            current_num = digit
        else:
            return False

    return True

t = int(raw_input())
for i in xrange(1, t + 1):
    n = [int(s) for s in raw_input().split(" ")]
    last_num = n[0]

    if isTidy(last_num):
        print "Case #{}: {}".format(i, int(last_num))
        continue
    else:
        last_num -= 1
        while last_num > 0:
            if isTidy(last_num):
                print "Case #{}: {}".format(i, int(last_num))
                break
            else:
                last_num -= 1