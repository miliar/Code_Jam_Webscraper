from math import pow


def insert_people(stalls, people):
    idx = 0
    parts = [(stalls-1)/2, stalls/2]

    result = None
    while idx < people:
        if idx == 0:
            result = (max(parts), min(parts))
        else:
            max_index = parts.index(max(parts))
            upperbound = parts[max_index]
            lowerbound = upperbound - 1 if upperbound > 0 else upperbound

            result = (upperbound/2, lowerbound/2)
            parts[max_index] = upperbound/2
            parts.append(lowerbound/2)

        idx += 1
    return result

#print insert_people(10,7)
#raise
with open(r'D:\PycharmProjects\GCJ_2017\C-small-1-attempt1.in', 'r') as inp:
    with open(r'D:\PycharmProjects\GCJ_2017\C-small-1-attempt1.out', 'w') as outp:
        idx = 0
        nr_tc = 0
        for line in inp:
            if idx == 0:
                nr_tc = int(line.strip())
            else:
                l = line.strip().split()
                stalls, people = long(l[0]), long(l[1])
                maximum, minimum = insert_people(stalls, people)
                outp.write('Case #%s: %s %s\n' % (idx, maximum, minimum))
            idx += 1