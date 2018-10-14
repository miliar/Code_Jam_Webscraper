#!/usr/bin/env python2.7
# -*- coding: utf8 -*-


def make_recycled(strnum):
    result = []
    for _ in range(len(strnum)):
        strnum = ''.join([strnum[-1],strnum[:-1]])
        result.append(int(strnum))

    return result

with open('C-small-attempt0.in', 'r') as f:
    with open('C-small-out', 'w') as out:
        count = int(f.readline())

        for i, line in enumerate(f):
            try:
                a = int(line.split()[0])
                b = int(line.split()[1])

                count_rec = 0

                result = {}
                for number in range(a, b+1):
                    for recycled in make_recycled(str(number)):
                        if a <= recycled and recycled <= b and recycled != number and recycled > 9:

                            if recycled in result:
                                if number not in result[recycled]:
                                    result[recycled].append(number)
                                    count_rec += 1

                            elif number in result:
                                if recycled not in result[number]:
                                    result[number].append(recycled)
                                    count_rec += 1

                            else:
                                result.update({number:[recycled]})
                                count_rec += 1

                #print 'Case #%d : %d' % (i+1, count_rec)
                out.write('Case #%d: %d\n' % (i+1, count_rec))

            except IndexError:
                pass


