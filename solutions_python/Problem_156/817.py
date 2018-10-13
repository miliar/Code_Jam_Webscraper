import sys

OUT_FILE = "output"

def parse_input(fd):
    nb_testcases = int(fd.readline())
    with open(OUT_FILE, "w") as out_fd:
        for case_number in xrange(0, nb_testcases):
            line1 = fd.readline().strip()
            line2 = fd.readline().strip()

            D = int(line1)
            pans = line2.split(" ")

            ###########################"
            vals = []
            for col in xrange(D):
                pan_remain = int(pans[col])
                vals.append(pan_remain)
                mul = 1
                while pan_remain > 1:
                    pan_remain = (pan_remain >> 1) + (pan_remain & 0x1)
                    mul <<= 1
                    for i in xrange(mul):
                        vals.append(pan_remain)
            vals.sort(reverse=True)

            res = -1
            for i, val in enumerate(vals):
                val += i
                if res < 0 or res > val:
                    res = val
                vals[i] = val

            real_res = res

            ##############################

            vals = []
            for col in xrange(D):
                pan_remain = int(pans[col])
                vals.append(pan_remain)
                mul = 1
                while pan_remain > 1:
                    if pan_remain == 9:
                        vals.append(3)
                        vals.append(6)
                        pan_remain = 6
                    else:
                        pan_remain = (pan_remain >> 1) + (pan_remain & 0x1)
                        mul <<= 1
                        for i in xrange(mul):
                            vals.append(pan_remain)
            vals.sort(reverse=True)

            res = -1
            for i, val in enumerate(vals):
                val += i
                if res < 0 or res > val:
                    res = val
                vals[i] = val

            ##############################

            print "Case #%d: %d" % (case_number + 1, min(real_res, res))
            out_fd.write("Case #%d: %d\n" % (case_number + 1, min(real_res, res)))

parse_input(sys.stdin)
