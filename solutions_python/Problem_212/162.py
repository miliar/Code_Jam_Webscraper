# python 3.4 !!

from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

@lru_cache(maxsize = None)
def dp3(x1, x2, m):
    if x1 == 0 and x2 == 0:
        return 0
    else:
        extra = 0
        if m == 0:
            extra = 1
        remove_x1 = 0
        if x1 >= 1:
            remove_x1 = dp3(x1-1, x2, (m+1)%3)
        remove_x2 = 0
        if x2 >= 1:
            remove_x2 = dp3(x1, x2-1, (m+2)%3)
        return extra + max(remove_x1, remove_x2)

@lru_cache(maxsize = None)
def dp4(x1, x2, x3, m):
    if x1 == 0 and x2 == 0 and x3 == 0:
        return 0
    else:
        extra = 0
        if m == 0:
            extra = 1
        remove_x1 = 0
        if x1 >= 1:
            remove_x1 = dp4(x1-1, x2, x3, (m+1)%4)
        remove_x2 = 0
        if x2 >= 1:
            remove_x2 = dp4(x1, x2-1, x3, (m+2)%4)
        remove_x3 = 0
        if x3 >= 1:
            remove_x3 = dp4(x1, x2, x3-1, (m+3)%4)
        return extra + max(max(remove_x1, remove_x2), remove_x3)


def compute():
    dp3.cache_clear()
    dp4.cache_clear()

    N, P = map(int, input().split())

    G = list(map(int, input().split()))

   # print(N, P)
   # print(G)

    mod_count = [0,0,0,0]
    for x in G:
        mod_count[x % P] += 1

    if P == 2:
        return mod_count[0] + ((mod_count[1]+1) // 2)
    elif P == 3: 
        return mod_count[0] + dp3(mod_count[1], mod_count[2], 0)
    else: # P == 4:
        return mod_count[0] + dp4(mod_count[1], mod_count[2], mod_count[3], 0)

    return 0

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
