from heapq import heappush, heappop

def choose_stall(longest):
    taken = longest // 2
    if longest % 2 == 0: # even
        left = taken - 1
        right = taken
    else: # odd
        left = taken
        right = taken
    return (left, right)



def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(' ')]
        queue = []
        heappush(queue, (-n, n))
        y = 0
        z = 0
        if n != k:
            for j in range(0, k - 1):
                longest = heappop(queue)[1]
                left, right = choose_stall(longest)
                if left != 0:
                    heappush(queue, (-left, left))

                if right != 0:
                    heappush(queue, (-right, right))

            longest = heappop(queue)[1]
            left, right = choose_stall(longest)
            y = max(left, right)
            z = min(left, right)

        print('Case #{}: {} {}'.format(i, y, z))

if __name__ == '__main__':
    main()

