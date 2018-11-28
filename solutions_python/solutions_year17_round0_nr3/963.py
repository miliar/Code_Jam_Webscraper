import sys

my_cache = {}

def get_max_min(n, k):
    assert(n >= k)
    if (n == k):
        return 0, 0
    if my_cache.has_key((n, k)):
        return my_cache[(n, k)]
    if k == 1:
        return n/2, (n-1)/2
    elif k == 2:
        return get_max_min(n/2, 1)
    l_max, l_min = get_max_min((n-1)/2, (k-1)/2)
    r_max, r_min = get_max_min(n/2, k/2)

    if l_min < r_min:
        my_cache[(n, k)] = (l_max, l_min)
        return l_max, l_min
    elif l_min == r_min and l_max < r_max:
        my_cache[(n, k)] = (l_max, l_min)
        return l_max, l_min
    my_cache[(n, k)] = (r_max, r_min)
    return r_max, r_min

t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    my_cache.clear()
    my_max, my_min = get_max_min(n, k)
    print ("Case #{}: {} {}".format(i, my_max, my_min))

        
