filename = "aLarge.in"
outputFilename = "output.txt"


def flip(arr, first, last):
    # print "---"
    # print arr, first, last
    for i in range(first, last):
        arr[i] = 1 - arr[i]
    # print arr

def solve(f):
    line = f.readline().strip().split(" ")
    arr = map(lambda c: 1 if c == '+' else 0, line[0])
    backup = arr[:]
    size = int(line[1])
    forward = 0
    backward = 0
    i = 0
    while i + size -1 < len(arr):
        if not arr[i]:
            flip(arr, i, i + size)
            forward += 1
        i += 1

    # print "========="

    arr = backup

    i = len(arr) - 1
    while i - size + 1 >= 0:
        if not arr[i]:
            flip(arr, i - size + 1, i + 1)
            backward += 1
        i -= 1

    if all(arr):
        return min(forward, backward)

    return "IMPOSSIBLE"


def out(s, o):
    print s
    o.write("{}\n".format(s))


def main():
    f = open(filename)
    o = open(outputFilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1


if __name__ == "__main__":
    main()
