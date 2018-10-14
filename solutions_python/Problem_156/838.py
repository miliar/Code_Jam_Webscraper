import math

def solve(dist):
    max_height = math.ceil(sum(dist))
    return min([get_total(h, dist) for h in range(1, max_height + 1)])
        
def get_total(height, dist):
    return sum([(i - 1) // height for i in dist]) + height

num_test = int(input())
for i in range(num_test):
    total = int(input())
    dist = [int(i) for i in input().split()]
    print("Case #{0}: {1}".format(i+1, solve(dist)))
