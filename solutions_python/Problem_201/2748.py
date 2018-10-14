import math

def BathroomStalls(N, K):
    queue = [N]
    while K > 1:
        if math.ceil((N-1)/2) != 0:
            queue.append(math.ceil((N-1)/2))
        if math.floor((N-1)/2):
            queue.append(math.floor((N-1)/2))
        K -= 1
        queue = sorted(queue[1:])[::-1]
        N = queue[0]

    return(math.ceil((N-1)/2), math.floor((N-1)/2))

t = int(input())
for i in range(1, t + 1):
    params = input().split(" ")
    params = [int(i) for i in params]
    output = BathroomStalls(params[0], params[1])
    print("Case #{}: {} {}".format(i, output[0], output[1]))
