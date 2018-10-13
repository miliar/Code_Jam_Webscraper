import sys
import numpy as np

def get_minimum_friends(l):
    deficiency = []
    for i, j in enumerate(np.cumsum(l)):
        d = (i+1)-j
        if d > 0:
            deficiency.append(d)

    return max(deficiency) if len(deficiency) else 0

def convert_string_to_list(l):
    return map(int, l)

if __name__=='__main__':
    count = 0
    for i in sys.stdin:
        if count == 0:
            count += 1
            continue
        _, l = i.split()

        print 'Case #%d:' % count, get_minimum_friends(convert_string_to_list(l))
        count += 1
