def spli(n):
    if n % 2 == 0:
        return (n // 2 - 1, n // 2)
    else:
        return (n // 2, n // 2)

def fu(n, k):
    gr_size = n
    gr_num = 1
    sm_size = n - 1
    sm_num = 0

    while True:
        #print("{} {}".format(gr_size, sm_size))
        assert(gr_size - 1  == sm_size)
        new_gr_size = gr_size // 2
        new_sm_size = gr_size // 2 - 1

        if gr_size % 2 == 0:
            new_gr_num = gr_num
            new_sm_num = gr_num + 2 * sm_num
        else:
            new_gr_num = gr_num * 2 + sm_num
            new_sm_num = sm_num

        if k <= gr_num:
            return spli(gr_size)
        else:
            k -= gr_num

        if k <= sm_num:
            return spli(sm_size)
        else:
            k -= sm_num


        gr_size = new_gr_size
        gr_num = new_gr_num
        sm_size = new_sm_size
        sm_num = new_sm_num

# def fu2(n, k):
#     li = [n]
#     for i in range(0, k - 1):
#         gr = li.pop()
#         (a, b) = spli(gr)
#         li.append(a)
#         li.append(b)
#         li.sort()
#     return spli(li.pop())
#
# for n in range(1, 100):
#     for k in range(1, n):
#         assert(fu(n, k) == fu2(n, k))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(x) for  x in  input().split(" ")]  # read a list of integers, 2 in this case

    mi, ma = fu(n, k)
    print("Case #{}: {} {}".format(i, ma, mi))
