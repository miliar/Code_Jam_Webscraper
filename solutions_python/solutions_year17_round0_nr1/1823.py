def flip(row, index, flipper_size):
    count = 0
    while count < flipper_size:
        row[index] = not(row[index])
        count += 1
        index += 1
    return row


with open(r'D:\PycharmProjects\GCJ_2017\A-large.in', 'r') as inp:
    with open(r'D:\PycharmProjects\GCJ_2017\A-large.out', 'w') as outp:
        idx = 0
        nr_tc = 0
        for line in inp:
            if idx == 0:
                nr_tc = int(line.strip())
            else:
                l = line.strip().split()
                row, flipper = [e == '+' for e in l[0]], long(l[1])
                index = 0
                flips = 0
                while index+flipper<=len(row):
                    if not row[index]:
                        row = flip(row, index, flipper)
                        flips += 1
                        index += 1
                    else:
                        index += 1

                while index<len(row):
                    if not row[index]:
                        flips = 'IMPOSSIBLE'
                        break
                    index += 1

                #print 'Case #%s: %s\n' % (idx, flips)
                outp.write('Case #%s: %s\n' % (idx, flips))
            idx += 1