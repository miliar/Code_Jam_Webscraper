n = int(input())
for q in range(n):
    n, k = map(int, input().split())
#      print(n, k)
    used = 0
    level = 0
    small_size = n
    while used+2**level < k:
        used += 2**level
        level += 1
        small_size = (small_size-1)//2

    # I have `free` free stalls that will be divided in 2**level blocks
    free = n - used
    blocks = 2**level

    nlarge = free % blocks
    nsmall = blocks - nlarge
    k -= used
#      print("After placing", used, "I have", nsmall, "small and", nlarge, "large, where small have size", small_size)

    if k > nlarge: # will use small block
        rs = ls = (small_size - 1) // 2
        if small_size % 2 == 0:
            rs = ls + 1
    else: # will use large block
        rs = ls = (small_size + 1 - 1) // 2
        if small_size % 2 == 1:
            rs = ls + 1

    print("Case #{}: {} {}".format(q+1, rs, ls))
