import heapq

tc = int(input())

for t in range(tc):
    n, k = input().split()
    n = int(n)
    k = int(k) - 1

    lengths = [-n]
    amounts = {n: 1}

    while True:
        largest = -heapq.heappop(lengths)
        amount = amounts.pop(largest)
        left = (largest - 1) // 2
        right = largest - 1 - left
        if amount > k:
            print("Case #%d: %d %d" % (t+1, right, left))
            break
        k -= amount
        if left not in amounts:
            heapq.heappush(lengths, -left)
            amounts[left] = 0
        amounts[left] += amount
        if right not in amounts:
            heapq.heappush(lengths, -right)
            amounts[right] = 0
        amounts[right] += amount

