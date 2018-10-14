# (R, C, X)
winnable_configuration = {
    (1, 1, 2): False,
    (1, 1, 3): False,
    (1, 1, 4): False,

    (1, 2, 2): True,
    (1, 2, 3): False,
    (1, 2, 4): False,

    (1, 3, 2): False,
    (1, 3, 3): False,
    (1, 3, 4): False,

    (1, 4, 2): True,
    (1, 4, 3): False,
    (1, 4, 4): False,

    (2, 2, 2): True,
    (2, 2, 3): False,
    (2, 2, 4): False,

    (2, 3, 2): True,
    (2, 3, 3): True,
    (2, 3, 4): False,

    (2, 4, 2): True,
    (2, 4, 3): False,
    (2, 4, 4): False,

    (3, 3, 2): False,
    (3, 3, 3): True,
    (3, 3, 4): False,

    (3, 4, 2): True,
    (3, 4, 3): True,
    (3, 4, 4): True,

    (4, 4, 2): True,
    (4, 4, 3): False,
    (4, 4, 4): True
}

if __name__ == "__main__":
    with open("input.txt", "r") as input, open("output.txt", "w") as output:
        T = int(input.readline())
        for t in range(T):
            tokens = input.readline().split(" ")
            X = int(tokens[0])
            R = int(tokens[1])
            C = int(tokens[2])
            winnable = True
            r = min(R, C)
            c = max(R, C)
            if X == 1:
                winnable = True
            else:
                winnable = winnable_configuration[(r, c, X)]
            print("Case #{0}: {1}".format(t + 1, "GABRIEL" if winnable else "RICHARD"), file=output)