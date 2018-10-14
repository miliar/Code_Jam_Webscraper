# -*- coding: utf-8 -*-


def solove():

    case_num = int(raw_input())
    for i in range(1, case_num + 1):
        case_line = raw_input().strip().split()
        c = float(case_line[0])
        f = float(case_line[1])
        x = float(case_line[2])

        remain = x
        speed = float(2)

        spend_time = float(0)

        while abs(remain - 0) > 0.000001:

            if remain <= c:
                spend_time += remain / speed
                break
            #accumulate c cookies and decide wheather buy a farm or not
            s = c / speed
            spend_time += s

            speed_buy = speed + f

            t1 = remain / speed_buy
            t2 = (remain - c) / speed

            if t1 < t2:
                speed = speed_buy
            else:
                remain = remain - c
        print "Case #%d: %.7f" % (i, spend_time)





if __name__ == "__main__":
    solove()
