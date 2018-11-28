import queue

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

    n, k = [int(s) for s in input().split(" ")]


# n = 1000
# k = 1000
# for i in range(1):

    l = {n: 1}
    q = queue.PriorityQueue()
    q.put_nowait(-n)
    left = 0
    right = 0
    while k > 0:
        longest = -q.get_nowait()
        num = l.pop(longest, 0)
        k -= num

        longest -= 1
        left = longest >> 1
        right = longest - left

        for fish in (left, right):
            if fish in l:
                l[fish] += num
            else:
                l[fish] = num
                q.put_nowait(-fish)

    print("Case #{}: {} {}".format(i, right, left))

