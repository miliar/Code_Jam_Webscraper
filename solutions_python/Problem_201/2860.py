import math
from math import *

#N = 4, -1, 4 -> 1
#N = 3, -1, 3 -> 1
#
def between(x,y):
    place = math.floor((y - x) / 2) + x
    l_s = place - x - 1
    l_r = y - place - 1
    return (place, l_s, l_r)


def ins(stalls):
    l_s = -1
    r_s = -1
    place_s = -1
    index = -1
    for i in range(len(stalls) - 1):
        (place, l, r) = between(stalls[i], stalls[i+1])
        if min(l,r) > min(l_s, r_s) or (min(l,r) == min(l_s, r_s) and max(l,r) > max(r_s, l_s)):
            (place_s, l_s, r_s) = (place, l, r)
            index = i+1

    stalls.insert(index, place_s)
    return (stalls, l_s, r_s)


t = int(input())  # read a line with a single integer
for i in range(t):
    line = input()
    nums= line.split()
    N = int(nums[0])
    K = int(nums[1])

    stalls = [-1, N]
    for j in range(K):
        (stalls, l, r) = ins(stalls)
    print ('Case #{}: {} {}'.format(i + 1, r, l))


'''




N = 100
stalls = [-1, N]
K = 5
for i in range(1, K+1, 1):
    (stalls, l, r) = ins(stalls)
    #print(1000000 / math.log(i+2, 2))

    guess = N / 2**ceil(log2(i+1))

    print (i, l, r, log2(i+1), ceil(log2(i+1))+1, i - 2**(ceil(log2(i+1))-1), guess) #, 100 / l, 100 / 2**ceil(log2(i+2)))

N = 1000000
K = 5

queue = [N]

for i in range (K): #(ceil(log2(K+1))+1):
    m = queue.pop(0)
    if m % 2 == 0:
        queue.append(int(m / 2))
        queue.append(int(m / 2 - 1))
    else:
        queue.append(int(m / 2))
        queue.append(int(m / 2))
print (queue)

#stalls = [-1, N]
#for i in range(1, K+1, 1):
#    (stalls, l, r) = ins(stalls)
#print (l,r)

'''

