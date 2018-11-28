fi = open("C-small-attempt1.in", 'r')
fo = open("C-small-out-1.txt", 'w')

table = {
    # a *  b = result * sign (+1/-1)
    ("1", "1"): ("1", 1),
    ("1", "i"): ("i", 1),
    ("1", "j"): ("j", 1),
    ("1", "k"): ("k", 1),
    ("i", "1"): ("i", 1),
    ("i", "i"): ("1", -1),
    ("i", "j"): ("k", 1),
    ("i", "k"): ("j", -1),
    ("j", "1"): ("j", 1),
    ("j", "i"): ("k", -1),
    ("j", "j"): ("1", -1),
    ("j", "k"): ("i", 1),
    ("k", "1"): ("k", 1),
    ("k", "i"): ("j", 1),
    ("k", "j"): ("i", -1),
    ("k", "k"): ("1", -1),
}

# Multiplies two tuples of value, sign
def multiply(a, b):
    multiplied = table[(a[0], b[0])]
    sign = a[1] * b[1] * multiplied[1]
    return (multiplied[0], sign)

def reduces_to_one(string):
    if len(string) == 0:
        return True
    buf = (string[0], 1)
    for i in xrange(1, len(string)):
        buf = multiply(buf, (string[i], 1))
    return buf == ("1", 1)

# Maps progress to char
goal = (("i", 1), ("j", 1), ("k", 1))

T = int(fi.readline())

for case in xrange(1, T + 1):
    L, X = [int(x) for x in fi.readline().split()]
    inp = fi.readline().rstrip()

    # Go greedily then check end reduces to 1
    progress = 0

    # this wont work for large input
    chars = inp * X
    i = 1
    buf = (chars[0], 1)
    while progress < 3 and i < len(chars):
        if buf == goal[progress]:
            # yaaay
            progress += 1
            if progress == 3:
                break #fixes a bug
            buf = (chars[i], 1)
        else:
            # multiply and continue
            buf = multiply(buf, (chars[i], 1))
        i += 1

    # Either ran out of chars or finished
    result = "NO"
    if progress == 3 and reduces_to_one(chars[i:]):
        result = "YES"
    elif progress == 2 and buf == goal[2]:
        result = "YES"

    fo.write("Case #{}: {}\n".format(case, result))



fi.close()
fo.close()
