# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    N = int(input())
    m = list(map(int, input().split()))
    
    maxdiff = 0

    count1 = 0
    prev = 0
    for mi in m:
        diff = prev - mi
        if diff >= 0:
            count1 += diff
            if diff > maxdiff:
                maxdiff = diff             
        prev = mi
    answer1 = count1
    
    rate = maxdiff
    count2 = 0
    for mi in m[:-1]:
        count2 += min(rate, mi)

    answer2 = count2

    return str(answer1) + " " + str(answer2)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
