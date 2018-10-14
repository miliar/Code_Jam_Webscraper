import logging
import Queue as Q
import math

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(n, k):
    if k * 2 > n:
        return 0, 0
    q = Q.PriorityQueue()
    q.put(-n)
    while not q.empty():
        cur = -q.get()
        k -= 1
        a, b = cur / 2, (cur-1) / 2
        if k == 0:
            return a, b
        q.put(-a)
        q.put(-b)

    assert(False)
    return -1

def compute2(n, k):
    magic_pow = int(math.log(k) / math.log(2))
    magic_num = 2 ** magic_pow
    availables = n / magic_num
    if k - magic_num <= n % magic_num:
        return availables/2, (availables-1) / 2
    return (availables-1)/2,(availables-2) / 2

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    n,k = [int(s) for s in raw_input().split(" ")]
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    result = compute2(n,k)
    print "Case #{}: {} {}".format(i, result[0], result[1])
