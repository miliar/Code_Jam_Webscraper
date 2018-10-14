def get_tidy_num(case_no, n):
    i = 0
    done = False
    tidy_num = 0
    pending_digit = n[0]
    pending_count = 0
    for i in xrange(len(n)):
        if not done:
            if n[i] == pending_digit:
                pending_count += 1
            elif n[i] > pending_digit:
                while pending_count > 0:
                    tidy_num *= 10
                    tidy_num += int(pending_digit)
                    pending_count -= 1
                pending_count = 1
                pending_digit = n[i]
            else:
                done = True
                tidy_num *= 10
                tidy_num += int(pending_digit) - 1
                pending_count -= 1
                while pending_count > 0:
                    tidy_num *= 10
                    tidy_num += 9
                    pending_count -= 1
                tidy_num *= 10
                tidy_num += 9
        else:
            tidy_num *= 10
            tidy_num += 9

    if not done and pending_count > 0:
        while pending_count > 0:
            tidy_num *= 10
            tidy_num += int(pending_digit)
            pending_count -= 1

    return "Case #{0}: {1}".format(case_no+1, tidy_num)



if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(0, t):
        n = raw_input()
        print get_tidy_num(i, n)
