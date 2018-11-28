
from bitarray import bitarray


def solve(k, pancakes):
    cnt = 0
    for i in range(len(pancakes)+1-k):
        if not pancakes[i]:
            pancakes[i:i+k] = ~pancakes[i:i+k]
            cnt += 1
    if pancakes.all():
        return cnt
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1, T+1):
        pancakes, k = raw_input().strip().split()
        k = int(k)
        pancakes = bitarray([c == "+" for c in pancakes])

        print "Case #%d: %s" % (t, str(solve(k, pancakes)))
