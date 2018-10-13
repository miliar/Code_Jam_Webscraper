import heapq


def number_stalls(left, right):
    return abs(right - left) - 1


def insert_one(locations):
    _, (Ls, Rs) = heapq.heappop(locations)
    stall = (Ls + Rs) // 2
    heapq.heappush(locations, ((-number_stalls(Ls, stall), stall), (Ls, stall)))
    heapq.heappush(locations, ((-number_stalls(stall, Rs), Rs), (stall, Rs)))

    return stall, number_stalls(Ls, stall), number_stalls(stall, Rs)


def stall(n, k):
    '''location = ((- #stalls between Ls&Rs, Rs), (Ls, Rs))'''
    # Initially: only guards, in stalls 0 and n+1
    locations = [((-number_stalls(0, n+1), n+1), (0, n+1))]

    for _ in range(k):
        _, left, right = insert_one(locations)

    return '{} {}'.format(max(left, right), min(left, right))


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, k = map(int, input().split())
        print('Case #{t}: {v}'.format(t=i+1, v=stall(n, k)))
