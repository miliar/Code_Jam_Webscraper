import itertools

def multiset(D):
    # print(D)
    L = [0] * (1 + max(D))
    for n in D:
        L[n] += 1
    return tuple(L)

memo = {}
def t(L):
    if L in memo:
        return memo[L]
    
    index_max, value_max = L[-1], len(L)-1
    if value_max <= 1:
        return value_max
    res = min(
        itertools.chain(
            (value_max,),
            (1 + t(splitted(L, n)) for n in range(1, value_max))
        )
    )
    memo[L] = res
    return res
        
def splitted(L, n):
    index_max, value_max = L[-1], len(L)-1
    
    L2 = list(L)
    L2[-1] -= 1
    
    new_value = value_max - n
    L2[new_value] += 1
    L2[n] += 1
    
    while L2[-1] == 0:
        del L2[-1]
    
    return tuple(L2)

def parse(inputfilename):
    it = iter(open(inputfilename))
    N = int(next(it))
    for i in range(N):
        G = int(next(it))
        print("Case #{}: {}".format(i+1, t(multiset(tuple(map(int, next(it).split()))))))
        
parse("B-small-attempt0.in")