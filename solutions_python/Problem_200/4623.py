import asyncio


async def is_tidy(num):
    l = str(num)
    return all(a <= b for a, b in zip(l[:-1], l[1:]))


async def main():
    T = int(input())

    for i in range(1, T + 1):
        N = int(input())
        while N > 0:
            if await is_tidy(N):
                print(f'Case #{i}: {N}')
                break
            N -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print('Exception at main!')
        print(f'{e}')
    finally:
        loop.close()
