def flip(arr, idx, size):
    for i in range(idx, idx + size):
        if i >= len(arr):
            return None
        assert arr[i] == "+" or arr[i] == "-"
        if arr[i] == "-":
            arr[i] = "+"
        else:
            arr[i] = "-"
    return arr


def answer_question(s, k):
    arr = [x for x in s]
    i = 0
    flips = 0
    while i < len(arr):
        if arr[i] == "-":
            flips += 1
            arr = flip(arr, i, k)
            if arr is None:
                return "IMPOSSIBLE"
        i += 1
    return str(flips)


with open("input.txt", "r") as handle:
    writer = open("output.txt", "w")
    handle.readline()
    idx = 1
    for x in handle:
        x = x[:-1]
        if len(x) == 0:
            continue
        split = x.split(" ")
        pancakes = split[0]
        k = int(split[1])
        func_out = answer_question(pancakes, k)

        print(idx, "-", x, func_out)

        answer = "Case #" + str(idx) + ": " + func_out
        writer.write(answer + "\n")
        idx += 1
