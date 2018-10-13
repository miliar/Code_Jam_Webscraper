

def get_bathroom(n, a, b, k):
    if k <= a:
        return n
    elif k <= a + b:
        return n-1
    else:
        if n % 2 == 1:
            new_n = (n - 1)/2
            new_a = a + a + b
            new_b = b
        else:
            new_n = n/2
            new_a = a
            new_b = a + b + b
        return get_bathroom(new_n, new_a, new_b, k-a-b)

def get_bathroom_num(n, k):
    num = get_bathroom(n, 1, 0, k)
    if num % 2 == 1:
        a = (num-1) / 2
        b = (num-1) / 2
    else:
        a = num / 2
        b = num / 2 - 1
    return a, b

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(0, t):
        n, k = map(int, raw_input().split(" "))
        print "Case #{0}: {1} {2}".format(i+1, *get_bathroom_num(n, k))
