def foo(file):
    num_cases = int(file.readline()[:-1])
    for i in range(num_cases):
        file.readline()
        mushrooms = file.readline()[:-1].split(" ")
        length = len(mushrooms)
        alg1 = algorithm1(mushrooms, length)
        alg2 = algorithm2(mushrooms, length)
        print("Case #{0}: {1} {2}".format(i+1, alg1, alg2))



def algorithm1(mushrooms, length):
    prev = int(mushrooms[0])
    total = 0
    for i in range(1, length):
        now = int(mushrooms[i])
        if now < prev:
            total += prev - now
        prev = now
    return total


def algorithm2(mushrooms, length):
    largest_diff = 0
    prev = int(mushrooms[0])
    for i in range(1, length):
        now = int(mushrooms[i])
        if now < prev:
            largest_diff = max(largest_diff, prev - now)
        prev = now

    total = 0
    for i in range(length - 1):
        now = int(mushrooms[i])
        if now > largest_diff:
            total += largest_diff
        else:
            total += now
        prev = now

    return total

# file = open("tiny.in", "r")
file = open("A-large.in","r")
foo(file)
