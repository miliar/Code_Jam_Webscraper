# filename = "a.in"
filename = "aLarge.in"
outputFilename = "output.txt"


def show(arr):
    return "\n" + "\n".join(map(lambda r: "".join(r), arr))


def solve(f):
    r, c = map(int, f.readline().strip().split(" "))
    arr = []
    for i in range(r):
        arr.append(list(f.readline().strip()))

    for i in range(r):
        for j in range(1, c):
            if arr[i][j] == "?":
                arr[i][j] = arr[i][j-1]
    print show(arr)

    for i in range(r):
        for j in range(c-2, -1, -1):
            if arr[i][j] == "?":
                arr[i][j] = arr[i][j+1]
    print show(arr)

    for i in range(1, r):
        for j in range(c):
            if arr[i][j] == "?":
                arr[i][j] = arr[i-1][j]
    print show(arr)

    for i in range(r-2, -1, -1):
        for j in range(c):
            if arr[i][j] == "?":
                arr[i][j] = arr[i+1][j]
    print show(arr)

    return show(arr)


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
