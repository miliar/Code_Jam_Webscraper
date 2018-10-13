# import Queue
#
# def foo(line):
#     args = line.split()
#     n, k = int(args[0]), int(args[1])
#     pq = Queue.PriorityQueue()
#     pq.put(-(n+1))
#     for i in xrange(k-1):
#         max_gap = -pq.get()
#         if max_gap == 1:
#             return "0 0"
#         half = max_gap / 2
#         pq.put(-(half + max_gap % 2))
#         pq.put(-half)
#     max_gap = -pq.get()
#     half = max_gap / 2 - 1
#     return "{0} {1}".format(half + max_gap % 2, half)

# def foo(line):
#     args = line.split()
#     n, k = int(args[0]), int(args[1])
#     n += 1
#     bound, num_levels = 2, 1
#     while k > bound - 1:
#         bound *= 2
#         num_levels += 1
#     diff = k - (bound / 2 - 1)
#     is_max_path = []
#     for _ in xrange(num_levels-1):
#         is_max_path.append(diff % 2 == 1)
#         diff = diff / 2 + diff % 2
#     is_max_path.reverse()
#     for is_max in is_max_path:
#         n = n / 2 + (n % 2 if is_max else 0)
#     if n <= 1:
#         return "0 0"
#     half = n / 2 - 1
#     return "{0} {1}".format(half + n % 2, half)

# def foo(line):
#     args = line.split()
#     n, k = int(args[0]), int(args[1])
#     max_path = []
#     while k > 1:
#         max_path.append(k % 2 == 0)
#         k /= 2
#     max_path.reverse()
#     max_gap = n + 1
#     for is_max in max_path:
#         max_gap = max_gap / 2 + (max_gap % 2 if is_max else 0)
#     if max_gap == 1:
#         return "0 0"
#     half = max_gap / 2 - 1
#     return "{0} {1}".format(half + max_gap % 2, half)

def foo(line):
    args = line.split()
    n, k = int(args[0]), int(args[1])
    gaps = [n+1]
    bound = 2
    while k > bound - 1:
        gaps = [half_gap for l in [[gap / 2 + gap % 2, gap / 2] for gap in gaps] for half_gap in l]
        bound *= 2
    gaps.sort()
    final_gap = gaps[bound - k - 1]
    final_half_gap = final_gap / 2
    return "0 0" if final_half_gap == 0 else "{0} {1}".format(final_half_gap + final_gap % 2 - 1, final_half_gap - 1)

if __name__ == "__main__":
    fo = open("output", "w")
    with open("C-small-2-attempt1.in") as f:
        text = [line.strip() for line in f.readlines()]
        [fo.write("Case #{0}: {1}\n".format(i, foo(text[i]))) for i in xrange(1, len(text))]
    fo.close()