import sys

filename = sys.argv[1]
f = open(filename)
T = int(f.readline())


def last_clean(number):
    result = []

    for i, c in enumerate(number):
        if i == 0:
            result.append(c)
            continue
        prev = int(number[i - 1])
        cur = int(c)

        if prev > cur:
            result.pop()
            result.append(str(prev - 1))
            result.append('9' * (len(number) - i))
            break
        else:
            result.append(c)

    return "".join(result)


def is_clean(number):
    for i in range(1, len(number)):
        prev = int(number[i - 1])
        cur = int(number[i])

        if cur < prev:
            return False
    return True
    

for t in range(T):
    number = f.readline().strip()
    while not is_clean(number):
        number = last_clean(number)

    print "Case #{}: {}".format(t + 1, int(number))
