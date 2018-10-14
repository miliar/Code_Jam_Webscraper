from math import floor, ceil, inf

epsilon = 10e-10

def to_tuple(x, ni):
    x = int(x)
    largest = floor(((x / ni) / 0.9) + epsilon)
    smallest = ceil(((x / ni) / 1.1) - epsilon)
    if not(largest * ni * 0.9 <= x and smallest * ni * 1.1 >= x):
        print ("FAILURE", x, ni)
        
    if ((largest + 1) * ni * 0.9 <= x or (smallest-1) * ni * 1.1 >= x):
        print ("FAILURE", x, ni)
    return (smallest, largest)
    
def main_code(t):
    N, P = tuple(map(int, input().split()))
    R = [int(x) for x in input().split()]
    Q = [sorted([to_tuple(x, R[n]) for x in input().split()]) for n in range(N)]
    result = 0
    
    while True:
        small_ind = -1
        failed = False
        bottom = -inf
        top = inf
        for i in range(N):
            if not Q[i]:
                print("Case #" + str(t) + ": " + str(result))
                return
            left, right = Q[i][0]
            if left > bottom:
                bottom = left
            if right < top:
                top = right
                small_ind = i
            if top < bottom:
                Q[small_ind] = Q[small_ind][1:]
                failed = True
                break
        if not failed:
            result += 1
            for i in range(N):
                Q[i] = Q[i][1:]
    

    

T = int(input())
for t in range(T):
    main_code(t + 1)
