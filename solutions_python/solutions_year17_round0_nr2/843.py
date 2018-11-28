def tidy(n):
    prev = n[0]
    for c in n:
        if c < prev:
            if (prev == "1"):
                return (len(n) - 1) * "9"
            else:
                first_occur = n.index(prev)
                return n[:first_occur] + str(int(prev) - 1) + "9" * (len(n) - first_occur - 1)
        prev = c
    return n

if __name__ == "__main__":
    with open("input") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(1, t + 1):
            n = fi.readline().strip()
            fo.write("Case #{}: {}\n".format(i, tidy(n)))
            print("Case #{}: {}\n".format(i, tidy(n)))
