from sortedcontainers import SortedList

def solve(n, k):
    l = SortedList([n])
    while k > 0:

        v = l[-1]
        v = v - 1
        del l[-1]
        
        to_add = [(v / 2) + (v % 2), v / 2]
        for a in to_add:
            if a > 0:
                l.add(a)
        
        k = k -1
    return to_add

def prev_power_of_2(x):
    return 2**((x).bit_length() - 1)


def solve_fast(n, k):
    small_path_size = prev_power_of_2(k)
    path_n = n - (2*small_path_size - 1)
    mod = path_n % small_path_size
    div = path_n / small_path_size
    k_small_path_size = k - small_path_size
    if k_small_path_size < mod:
        rv = div+1
    else:
        rv = div
    return [(rv / 2) + (rv % 2), rv / 2]

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        rv = solve_fast(n, k)
        print "Case #{}: {} {}".format(i, rv[0], rv[1])

if __name__ == "__main__":
    main()
