from collections import deque
t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    bath_array = [n]
    bath_array_num = [1]
    beki = 1

    while 2**beki-1 < m:

        if len(bath_array) == 2:
            for k in xrange(len(bath_array)):
                r = bath_array.pop()
                r_num = bath_array_num.pop()
                if r%2 == 0:
                    a = r/2 - 1
                    b = r/2
                    r_num_a = r_num
                    r_num_b = r_num
                if r%2 == 1:
                    c = (r-1)/2
                    r_num_c = r_num*2
            if a == c:
                r_num_a = r_num_a + r_num_c
            if b == c:
                r_num_b = r_num_b + r_num_c
            bath_array.append(a)
            bath_array.append(b)
            bath_array_num.append(r_num_a)
            bath_array_num.append(r_num_b)

        beki = beki + 1
        if len(bath_array) == 1:
            r = bath_array.pop()
            r_num = bath_array_num.pop()
            if r%2 == 0:
                a = r/2 - 1
                b = r/2
                r_num_a = r_num
                r_num_b = r_num
                bath_array.append(a)
                bath_array.append(b)
                bath_array_num.append(r_num_a)
                bath_array_num.append(r_num_b)
            if r%2 == 1:
                c = (r-1)/2
                r_num_c = r_num*2
                bath_array.append(c)
                bath_array_num.append(r_num_c)

    if 2**(beki-1)-1 + bath_array_num.pop() >= m:
        r = bath_array.pop()
        d = (r-1)/2
        e = (r-1)/2 + (r-1)%2
    else:
        r = bath_array.pop(0)
        d = (r-1)/2
        e = (r-1)/2 + (r-1)%2

    maxS = max([d,e])
    minS = min([d,e])
    print "Case #{}: {} {}".format(i, maxS, minS)

  # check out .format's specification for more formatting options
