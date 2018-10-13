import math

def split(n):
    if n%2 == 0:
        return [n//2, n//2]
    else:
        return [n//2+1, n//2]

def q3(n,k):
    l = math.floor(math.log(k,2))
    index = k - 2 ** l
    count = {n:1}  ## last dict
    cur = {}
    h = {n}  ##last list
    t = set()   ##current list
    for i in range(0,l):
        for j in h:
            if (j-1)%2==1:
                t.add(j//2)
                t.add(j//2-1)
                if j//2-1 in cur:
                    cur[j//2-1] += count[j]
                else:
                    cur[j//2-1] = count[j]
                if j//2 in cur:
                    cur[j//2] += count[j]
                else:
                    cur[j//2] = count[j]
            else:
                t.add((j-1)//2)
                if (j-1)//2 in cur:
                    cur[(j-1)//2] += 2* count[j]
                else:
                    cur[(j-1)//2] = 2* count[j]
        count = cur
        h = t
        t = set()
        cur = {}
    h=list(h)
    h.sort(key=lambda x: -x)
    return get(index, h, count) -1

def get(n, heap, dict):
    if n < dict[heap[0]]:
        return heap[0]
    else:
        return get(n-dict[heap[0]], heap[1:], dict)


total = int(input())


for c in range(1,total+1):
    numbers = [int(n) for n in input().split()]
    n = numbers[0]
    k = numbers[1]
    result = split(q3(n,k))
    print('Case #{0}: {1} {2}'.format(c, result[0], result[1]))
