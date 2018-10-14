t = int(raw_input())  # read a line with a single integer

def done(arr, k, flips):
    for i in range(len(flips)):
        if flips[i] == 1:
            for j in range(k):
                arr[i+j] = (arr[i+j] + 1)%2
    return all(map(lambda x: x==1, arr))


for i in xrange(1, t + 1):
    n, k = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    k = int(k)
    cakes = map(lambda x: 1 if x == "+" else 0, list(n))
    flips = [0]*len(cakes)
    flips[0] = 1-cakes[0]
    for j in range(1,len(cakes)-k+1):
        flips[j] = (cakes[j-1] - cakes[j] + (0 if j < k else flips[j-k])) % 2
    if done(cakes,k,flips):
        print 'Case #'+str(i)+': '+str(sum(flips))
    else:
        print 'Case #'+str(i)+': IMPOSSIBLE'