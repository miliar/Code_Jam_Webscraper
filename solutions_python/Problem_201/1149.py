
from collections import defaultdict

def solve(stalls, people):
    q = defaultdict(lambda: 0)
    q[stalls] = 1
    p = 1
    while p <= people:
        length = max(q)
        count = q[length]
        q.pop(length)
        minrl = (length - 1) // 2
        maxrl = minrl + (length - 1) % 2
        q[minrl] += count
        q[maxrl] += count
        p += count
    return str(maxrl) + " " + str(minrl)


def main():
    cases = int(input())
    for i in range(1, cases+1):
        stalls, people = tuple(int(x) for x in input().rstrip().split(" "))
        print("Case #%d: %s" % (i, solve(stalls, people)))

if __name__ == '__main__':
    main()

        