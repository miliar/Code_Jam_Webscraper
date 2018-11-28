t = int(input())  # read a line with a single integer
filep = open("p3small2.txt", 'w')
for i in range(1, t + 1):
    n, m = input().split(" ")
    n, m = int(n), int(m)
    empty = {n: 1}
    for j in range(m):
        largest = 0
        for s in empty:
            if s > largest:
                largest = s
        empty[largest] -= 1
        if empty[largest] == 0:
            empty.pop(largest)
        left = (largest - 1) // 2
        right = largest - 1 - left
        if left in empty:
            empty[left] += 1
        else:
            empty[left] = 1
        if right in empty:
            empty[right] += 1
        else:
            empty[right] = 1
    print("Case #{}: {} {}\n".format(i, max(left, right), min(left, right)))
    filep.write("Case #{}: {} {}\n".format(i, max(left, right), min(left, right)))


filep.close()
