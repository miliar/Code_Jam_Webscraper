def flip(pancakes, i, n):
    for c in range(i, i + n):
        pancakes[c] = 1 - pancakes[c]
    return pancakes

def check(pancakes, n):
    for i in range(len(pancakes) - n, len(pancakes)):
        if pancakes[i] == 0:
            return False
    return True

def convert(c):
    if c == "+":
        return 1
    else:
        return 0

with open("asdf.in") as f:
    with open("asdf.out", "w") as out:
        for l, line in enumerate(f):
            if l == 0 or line == "\n":
                continue
            pancakes, n = line.rstrip().split(" ")
            n = int(n)
            pancakes = [convert(c) for c in pancakes]
            flips = 0
            if check(pancakes, len(pancakes)):
                out.write("Case #{}: {}\n".format(l, flips))
                continue
            for i in range(len(pancakes) - n + 1):
                if pancakes[i] == 0:
                    pancakes = flip(pancakes, i, n)
                    flips += 1

            if check(pancakes, n):
                out.write("Case #{}: {}\n".format(l, flips))
            else:
                out.write("Case #{}: IMPOSSIBLE\n".format(l))
