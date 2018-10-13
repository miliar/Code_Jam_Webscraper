# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    C, D, V = map(int, input().split())
    ds = list(map(int, input().split()))

    a = [False] * (V+1)
    a[0] = True

    for i in ds:
        b = list(a)
        for j in range(0, V+1-i):
            if a[j] == True:
                b[i+j] = True
        a = list(b)

#    print(a)
    num_new_denom = 0
    for i in range(0, V+1):
        if a[i] == False:
            num_new_denom += 1
            new_demon = i
            b = list(a)
            for j in range(0, V+1-i):
                if a[j] == True:
                    b[i+j] = True
            a = list(b)

    return num_new_denom

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
