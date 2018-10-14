def rl(f):
    return f.readline().strip()

def main():
    inp = open("C-large.in")
    out = open("C-large.out", "w")

    T = int(rl(inp))
    for i in range(1, T+1):
        N = int(rl(inp))
        values = map(int, rl(inp).split(" "))
        if reduce(lambda a, b: a ^ b, values) != 0:
            print >>out, "Case #%d: NO" % i
        else:
            m = sum(values) - min(values)
            print >>out, "Case #%d: %d" % (i, m)

    inp.close()
    out.close()

if __name__ == "__main__":
    main()
