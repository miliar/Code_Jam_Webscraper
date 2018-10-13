def methodOne(mushroom):
    """docstring for methodOne"""
    count = 0
    for i in range(len(mushroom) - 1):
        if mushroom[i] - mushroom[i+1] > 0:
            count += mushroom[i] - mushroom[i+1]

    return count

def methodTwo(mushroom):
    """docstring for methodTwo"""
    max = 0
    count = 0
    for i in range(len(mushroom) - 1):
        if mushroom[i] - mushroom[i+1] > max:
            max = mushroom[i] - mushroom[i+1]
    for i in range(len(mushroom) - 1):
        if mushroom[i] < max:
            count += mushroom[i]
        else:
            count += max
    return count

if __name__ == '__main__':
    # mushroom1 = [10, 5, 15, 5]
    # mushroom2 = [100, 100]
    # mushroom3 = [81, 81, 81, 81, 81, 81, 81, 0]
    # mushroom4 = [23, 90, 40, 0, 100, 9]
    # print methodOne(mushroom1), methodTwo(mushroom1)
    f = open("A-large.in")
    wr = open("res.txt", "w")
    i = 0
    j = 1
    for line in f:
        if i == 0:
            i += 1
            continue
        elif i % 2 == 0:
            mushroom = line.split()
            mushroom = map(int, mushroom)
            wr.write("Case #" + str(j) + ": " + str(methodOne(mushroom)) + " " + str(methodTwo(mushroom)) + "\n")
            j = j + 1
        i = i + 1
