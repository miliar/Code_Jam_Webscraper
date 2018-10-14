import Queue as Q

# def smallest_gap_man(n, k):
#     if n == k:
#         return (0, 0)
#     gaps = Q.PriorityQueue()
#     gaps.put(-n)
#     for i in xrange(k):
#         biggest_gap = -gaps.get()
#         half = (biggest_gap - 1)/2.0
#         smaller = int(half)
#         bigger = int(half + 1/2.0)
#         gaps.put(-smaller)
#         gaps.put(-bigger)
#     return (bigger, smaller)

def get_poss_gaps(n):
    l = [n]
    while l[len(l) - 1] > 1:
        last = l[len(l) - 1]
        if last % 2 == 1:
            l.append((last - 1)/2)
        else:
            if (last - 1)/2 %2 == 0:
                l.append((last - 1)/2 + 1)
                l.append((last - 1)/2)

            else:
                l.append((last - 1)/2)
                l.append((last - 1)/2 + 1)
    return sorted(list(set(l)), reverse=True)

def get_ans(d, k):
    if d.get(k) == None:
        return 0
    else:
        return d[k]

def get_occ(d, k):
    return 2*get_ans(d, 2*k + 1) + get_ans(d, 2*k) + get_ans(d, 2*k + 2)

def get_num_occurences(n):
    gaps = get_poss_gaps(n)
    d = {}
    for gap in gaps:
        if get_occ(d, gap) == 0:
            d[gap] = 1
        else:
            d[gap] = get_occ(d, gap)
    return d, gaps


def get_index(n, k):
    d, gaps = get_num_occurences(n)
    count = [d[key] for key in sorted(d.keys(), reverse=True)]
    total = count[0]
    index = 0
    while total < k:
        index += 1
        if index == len(count) - 1:
            return index, gaps
        total += count[index]
    return index, gaps

def smallest_gap(n, k):
    index, gaps = get_index(n, k)
    last = gaps[index]
    half = (last - 1)/2.0
    smaller = int(half)
    bigger = int(half + 1/2.0)
    return (bigger, smaller)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
#     inp = raw_input().split(" ")
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    b, s = smallest_gap(n, k)
    print "Case #{}: {} {}".format(i, b, s)
