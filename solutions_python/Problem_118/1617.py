def ispalindrome(x):
    return x == x[::-1]

# Redhead, blonde, brunette... Egads.
def withnhalfdigits(n, max_):
    assert n >= 1
    assert max_ >= 0
    num = (2**min(n - 1, 3) - 1) << (n - 1 - min(n - 1, 3))
    count = 0

    # num + 1 is the number of permutations
    for i in range(num + 1):
        k = bin((1 << (n - 1)) + i)[2:]
        if int(k + k[::-1]) ** 2 > max_:
            break
        # print(int(k + k[::-1]), int(k + k[::-1]) ** 2)
        count += 1
        for j in range(10):
            candidate = int(k + str(j) + k[::-1])
            if candidate * candidate > max_:
                break
            if ispalindrome(str(candidate * candidate)):
                # print(candidate, candidate ** 2)
                count += 1

    k = str(2 * 10**(n - 1))
    pk = int(k + k[::-1])
    if pk * pk <= max_:
        # print(int(k + k[::-1]), int(k + k[::-1]) ** 2)
        count += 1
        for i in range(10):
            candidate = int(k + str(i) + k[::-1])
            if candidate ** 2 > max_:
                break
            if ispalindrome(str(candidate * candidate)):
                # print(candidate, candidate ** 2)
                count += 1

    return count

def nupto(n):
    c = 0

    if n >= 1:
        c += 1
    if n >= 4:
        c += 1
    if n >= 9:
        c += 1

    x = (len(str(n)) + 1) // 2
    for i in range(1, x + 1):
        c += withnhalfdigits(i, n)
    return c

with open("C-large-1.in", "rt") as infile:
    T = int(infile.readline())
    for i, line in enumerate(infile, 1):
        line = line.strip()
        if line:
            a, b = line.split(" ")
            a = int(a)
            b = int(b)
            nb = nupto(b)
            na = nupto(a - 1)
            # print("nb=%d, na=%d" % (nb, na))
            print("Case #%d: %d" % (i, nb - na))
