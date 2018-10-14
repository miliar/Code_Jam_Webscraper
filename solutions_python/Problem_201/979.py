import math

def floor(a, b):
    return a // b

def ceil(a, b):
    if a % b == 0:
        return a // b
    return a // b + 1

def decomp_power2(n):
    """ 
    Returns the greatest k such that 1 + 2 + 4 + ... + 2**k <= n 
    i.e. 2**(k+1) - 1 <= n
    i.e. k+1 = |_log2(n+1)_|
    """
    return math.floor(math.log2(n+1))-1

def solve(n, k):
    p = decomp_power2(k-1)
    # After 1 + 2 + ... + 2**p persons, the bathroom is decomposed into 2**(p+1) intervals
    nb_pers = 2**(p+1) - 1

    # All intervals are of one of these two lengths
    length_max =  ceil(n - nb_pers, nb_pers + 1)
    length_min = floor(n - nb_pers, nb_pers + 1)

    # There is a max intervals, and b min intervals,
    # i.e. n - nb_pers = a*length_max + b*length_min
    a = n - nb_pers - (nb_pers + 1) * length_min

    # The remaining persons get the largest intervals first
    if k - nb_pers <= a:
        # There is enough big intervals for everybody!
        interval = length_max
    else:
        # The last takes a small interval
        interval = length_min

    max, min = ceil(interval-1, 2), floor(interval-1, 2)
    print(n, k, '\t', max, min)
    #print("p", p, "nb_pers", nb_pers, "L", length_max, "l", length_min, "a", a)
    return "%d %d\n" %(max, min)


input_name = "C-small-2-attempt0"
out = open(input_name + ".out", "w")

with open(input_name + ".in", "r") as f:
    lines = f.readlines()

    t = int(lines[0])

    for i in range(1, t+1):
        n, k = map(int, lines[i].split())
        out.write("Case #%d: %s" % (i, solve(n, k)))

# def compute_distances(stalls, i):
#     """ i > 0 and i < n - 1 """
#     n = len(stalls)
#
#     ls = i
#     while not stalls[ls]:
#         ls -= 1
#     ls = i - ls
#
#     rs = i
#     while not stalls[rs]:
#         rs += 1
#     rs = rs - i
#
#     return ls, rs
#
# def choose(stalls):
#     """ stalls[i] = True <=> it is occupied """
#     n = len(stalls)
#
#     max_distance = 0
#     best_stalls = []
#
#     for i in range(n):
#         if not stalls[i]:
#             ls, rs = compute_distances(stalls, i)
#             d = min(ls, rs)
#
#             if d > max_distance:
#                 max_distance = d
#                 best_stalls = [(i, max(ls, rs))]
#             elif d == max_distance:
#                 best_stalls.append((i, max(ls, rs)))
#
#     if len(best_stalls) == 1:
#         return best_stalls[0][0]
#
#     best_stall = None
#     best_max = 0
#     for (stall, max_d) in best_stalls:
#         if best_max < max_d:
#             best_max = max_d
#             best_stall = stall
#
#     return best_stall
#
# def show(n):
#     stalls = [True] + [False]*n + [True]
#     choosed = [0]*(n+2)
#
#     for t in range(n):
#         i = choose(stalls)
#         stalls[i] = True
#         choosed[i] = t+1
#
#     return choosed
#
# for k in range(10):
#     print(show(k))