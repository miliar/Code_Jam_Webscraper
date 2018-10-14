# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def solve_r_1(C, W):
    return 

def compute():
    R, C, W = map(int, input().split())
    return (C//W) * (R-1) + (C-1)//W + W

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
