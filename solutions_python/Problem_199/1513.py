from pip._vendor.distlib.compat import raw_input


def flip(l, k):
    for i in range(k):
        if l[i] == "+":
            l[i] = "-"
        else:
            l[i] = "+"


def sol(s, k):
    count = 0
    pattern = "-" + "+" * (k - 1) + "-"
    l = [x for x in s]
    while len(l) != 0:
        while l[0] == "+":
            l.pop(0)
            if len(l) == 0:
                break
        if len(l) == 0:
            break
        if len(l) >= k:
            if (len(l) % (k + 1)) == 0:
                if pattern * int(len(l) / (k + 1)) == "".join(l):
                    count += 2 * (len(l) / (k + 1))
                    break
            flip(l, k)
            count += 1
        else:
            return 'IMPOSSIBLE'
    return int(count)

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t + 1):
        s, k = [x for x in raw_input().split(" ")]
        count = sol(s, int(k))
        print("Case #{}: {}".format(i, count))
