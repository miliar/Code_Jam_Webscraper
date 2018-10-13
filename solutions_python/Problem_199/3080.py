import fileinput

f = fileinput.input()
T = int(f.readline())


for case in range(T):

    pancakes, flip_size = f.readline().strip().split()
    n = len(pancakes)
    flip_size = int(flip_size)
    pancakes = list(map(lambda x: x == "+", pancakes))
    impossible = False
    flips = 0

    for i in range(n):
        if not pancakes[i]:
            if n - i < flip_size:
                impossible = True
                break
            for k in range(i, i + flip_size):
                pancakes[k] ^= True
            flips += 1

    flips = "IMPOSSIBLE" if impossible else flips
    print("Case #" + str(case + 1) + ":", flips)
