T = int(input())
test = 1

while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1
    line = input().split(" ")
    S = int(line[0])
    X = int(line[1])
    # print(S, X)
    line = input().split(" ")
    sizes = [int(i) for i in line]
    # print(sizes)
    sizes.sort()
    # print(sizes)
    start = 0
    end = S - 1
    count = 0
    while start <= end:
        if start == end:
            count += 1
            break
        if sizes[start] + sizes[end] <= X:
            start += 1
            end -= 1
            count += 1
            continue
        end -= 1
        count += 1
    print(count)