
import heapq


def person(bathroom):
    _, segment = heapq.heappop(bathroom)
    half = segment // 2
    if segment % 2 == 0:
        l, r = half, half - 1
    else:
        l, r = half, half
    for s in (l, r):
        if s > 0:
            heapq.heappush(bathroom, (-s, s))
    return l, r

def people(bathroom, k):
    last_segments = None, None
    while k > 0:
        last_segments = person(bathroom)
        k -= 1
    return last_segments

def make_bathroom(n):
    return [(-n, n)]

def main():
    t = int(input())
    for ti in range(1, t + 1):
        n, k = map(int, input().split())
        bathroom = make_bathroom(n)
        last_segments = people(bathroom, k)
        print("Case #{}: {x} {n}".format(
            ti,
            n=min(last_segments),
            x=max(last_segments)))

if __name__ == '__main__':
    main()
