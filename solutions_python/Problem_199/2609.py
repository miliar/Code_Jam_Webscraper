t = int(input())  # read a line with a single integer
filep = open("p1.txt", 'w')
for i in range(1, t + 1):
    count = 0
    n, m = input().split(" ") # read a list of integers, 2 in this case
    m = int(m)
    n = list(n)
    for j in range(len(n) - (m - 1)):
        if n[j] == '-':
            count += 1
            n[j] = '+'
            for k in range(1, m):
                if n[j+k] == '-':
                    n[j+k] = '+'
                else:
                    n[j+k] = '-'
    flipped = True
    for q in range(1, m):
        if n[-q] == '-':
            flipped = False
    if flipped:
        print("Case #{}: {}".format(i, count))
        filep.write("Case #{}: {}\n".format(i, count))
    else:
        filep.write("Case #{}: IMPOSSIBLE\n".format(i))
        print("Case #{}: IMPOSSIBLE".format(i))
filep.close()
