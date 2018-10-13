import asyncio
from itertools import starmap


class Stall:
    def __init__(self, S, LS, RS):
        self.S = S
        self.occupied = False
        self.LS = LS
        self.RS = RS


async def update_to_right(stalls, S):
    for i, stall in enumerate(stalls[S + 1:]):
        stall.LS = i
        if stall.occupied:
            break


async def update_to_left(stalls, S):
    for i, stall in enumerate(reversed(stalls[:S])):
        stall.RS = i
        if stall.occupied:
            break


async def search(stalls, function):
    for stall in stalls:
        stall.value = function(stall.LS, stall.RS)
    maximum = max(stall.value for stall in stalls)
    return list(filter(lambda stall: stall.value == maximum, stalls))


async def minmax(stalls):
    return await search(stalls, min)


async def maxmax(stalls):
    return await search(stalls, max)


async def choose_stall(stalls):
    filtered_stalls = list(filter(lambda stall: not stall.occupied, stalls))
    minSs = await minmax(filtered_stalls)
    if len(minSs) != 1:
        maxSs = await maxmax(minSs)
        return maxSs[0]
    return minSs[0]


async def result(stall):
    return max(stall.LS, stall.RS), min(stall.LS, stall.RS)


async def solve_stalls(i, stalls, K):
    for _ in range(K - 1):
        stall = await choose_stall(stalls)
        stall.occupied = True
        await update_to_left(stalls, stall.S)
        await update_to_right(stalls, stall.S)

    stall = await choose_stall(stalls)
    stall.occupied = True
    await update_to_left(stalls, stall.S)
    await update_to_right(stalls, stall.S)
    stall_result = await result(stall)
    print(f'Case #{i}: {stall_result[0]} {stall_result[1]}')


async def main():
    T = int(input())

    for i in range(1, T + 1):
        N, K = map(int, input().split())
        if N == K:
            print(f'Case #{i}: 0 0')
        else:
            stalls = [Stall(i, i, N - i - 1) for i in range(N)]
            await solve_stalls(i, stalls, K)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
