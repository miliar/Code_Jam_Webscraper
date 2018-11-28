def lastTidy(num):
    while num > 9:
        ls = list(str(num))
        if sorted(ls) == ls: return num
        num -= 1
    return num


if __name__ == "__main__":
    with open("in/B-small-attempt0.in") as data, open("out/B-small-attempt0.out", 'w') as res:
        size = int(data.readline())
        for i in xrange(1, size+1):
            res.write("Case #%d: %d\n" % (i, lastTidy(int(next(data)))))
