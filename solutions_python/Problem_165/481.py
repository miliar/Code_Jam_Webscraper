def check_size(r, c, w):
    if w == 1:
        return r * c
    if w == c:
        return r + w - 1
    if w > c / 2:
        return r + w
    if w == c / 2:
        return r + w + c%2
    if c % w == 0:
        return r * (c/w) + w - 1
    return r * (c/w) + w

if __name__ == "__main__":
    cases = []
    with open("A-small-attempt1.in") as f:
        f.readline()
        for line in f.readlines():
            cases.append(map(int, line.strip().split()))
    with open("output", "w") as f:
        for index, case in enumerate(cases):
            print "*"*80
            print case
            max_size = check_size(case[0], case[1], case[2])
            print("Case #{0}: {1}".format(index + 1, max_size))
            f.write("Case #{0}: {1}\n".format(index + 1, max_size))