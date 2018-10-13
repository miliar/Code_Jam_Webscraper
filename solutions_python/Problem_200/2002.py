def foo(line):
    arr = [int(c) for c in line]
    nine_idx = len(arr)
    for i in xrange(len(arr) - 1, 0, -1):
        if arr[i-1] > arr[i]:
            arr[i-1] -= 1
            for j in xrange(i, nine_idx):
                arr[j] = 9
            nine_idx = i
    return int(''.join([str(n) for n in arr]))

if __name__ == "__main__":
    fo = open("output", "w")
    with open("B-large.in") as f:
        text = f.readlines()
        text = [line.strip() for line in text]
        [fo.write("Case #{0}: {1}\n".format(i, foo(text[i]))) for i in xrange(1, len(text))]
    fo.close()