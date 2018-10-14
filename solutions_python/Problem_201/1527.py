import math
import numpy as np

def solve(n,k):
    logk = math.floor(math.log(k,2))
    num_bins = 2**logk
    if num_bins == 0:
        num_bins = 1
    my_rank = k - 2**logk
    bins = np.array([math.floor(ele) for ele in np.linspace(1,n+2,num_bins+1)])
    bin_sizes = bins[1:] - bins[:-1]
    sorted_bins = np.argsort(bin_sizes)[::-1]
    my_bin = sorted_bins[my_rank]
    my_L = bins[my_bin]
    my_R = bins[my_bin+1]
    mid = (my_L + my_R)//2
    Ls = mid - my_L - 1
    Rs = my_R - mid - 1
    y = int(max(Ls,Rs))
    z = int(min(Ls,Rs))
    return y,z

if __name__ == '__main__':
    t = int(input())
    for i in range(1,t+1):
        n,k = [int(s) for s in input().split(" ")]
        resulty,resultz=solve(n,k)
        print("Case #{}: {} {}".format(i, resulty,resultz))
