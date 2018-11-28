def two(n):
    return (n-1) / 2, n / 2

def comb(n, k):
    d = {n:1}
    j = 0
    while j < k:
        curr_n = max(d.keys())
        
        n1, n2 = two(curr_n)
        m = d[curr_n]
        d[n1] = d.get(n1, 0) + m
        d[n2] = d.get(n2, 0) + m
        j += m
        # for i in xrange(d[curr_n]):
            # n1, n2 = two(curr_n)
            # d[n1] = d.get(n1, 0) + 1
            # d[n2] = d.get(n2, 0) + 1
            # j += 1
            # print j, curr_n, n1, n2 
        
        d.pop(curr_n, None)
    return n2, n1
        


# print comb(4, 2)
# print comb(5, 2)
# print comb(6, 2)
# print comb(1000, 1000)

# print comb(1000, 1)
# import time
# q = 10 ** 18
# s1 = time.time()
# print comb(q, q / 100)
# s2 = time.time()
# print comb(q, q)
# e = time.time()
# print s2 - s1 
# print e - s2

res = []
with open("C-large.in") as f:
    t = int(f.readline().strip())
    print t
    for r in range(t):
        mn, mk = f.readline().strip().split(" ")
        mn, mk = int(mn), int(mk)
        my_res = comb(mn, mk)
        res.append(my_res)
        print mn, mk, my_res


        
with open("outCLarge.txt", "w") as out:
    for i, r in enumerate(res):
        out.write("Case #{}: {} {}\n".format(i+1, r[0], r[1]))
