def generate_tidy(n, i):
    k = n[:i] + str(int(n[i])-1)
    i += 1
    while i < len(n):
        k += '9'
        i += 1
    return k


def is_Tidy(k):
    i = len(k)-1
    while i > 0:
        if k[i] >= k[i-1]:
            i -= 1
        else:
            return False
    return True


def fast_find_largest_tidy(n):
    k = str(n)
    if is_Tidy(k):
        return n
    i = 0
    while i < len(k)-1:
        if k[i] < k[i+1]:
            i += 1
        else:
            return long(generate_tidy(k, i))
    return n


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = long(raw_input())
        print "Case #{}: {}".format(i, fast_find_largest_tidy(n))