import math
def bathroom(n,k):
    #construct stalls
    stall = [n + 2]
    h = math.floor(math.log2(k))
    s = n + 2
    for i in range(h):
        s = math.ceil((s + 1) / 2)
    
    j = (n + 1) % (2**h)
    if (j == 0 or (k - 2**h) < j):
        return (math.ceil((s + 1) / 2) - 2,\
            (s + 1) // 2 - 2)
    else:
        return (math.ceil(s / 2) - 2,\
             s // 2 - 2)

    # for i in range(k):
    #     s = max(stall)
    #     stall.remove(s)
    #     stall.append(math.ceil((s+1)/2))
    #     stall.append((s + 1)//2)
    #return tuple([i - 2 for i in stall[-2:]])
    


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = [int(s) for s in input().split()]  # read a list of integers, 2 in this case
  res = bathroom(n,k)
  print("Case #{}: {} {}".format(i, res[0], res[1]))
  # check out .format's specification for more formatting options