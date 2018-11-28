def rl(f):
    return f.readline().strip()

def main():
    inp = open("B-small-attempt0.in")
    out = open("B-small.out", "w")

    T = int(rl(inp))
    for i in range(1, T+1):
        line = rl(inp).split(" ")
        C, line = int(line[0]), line[1:]
        comb = {}
        for j in range(C):
            e1, e2, e3 = line.pop(0)
            comb[e1 + e2] = e3
            comb[e2 + e1] = e3

        D, line = int(line[0]), line[1:]
        opp = {}
        for j in range(D):
            e1, e2 = line.pop(0)
            opp[e1] = e2
            opp[e2] = e1

        N, s = line
        final = []
        prev = ""
        for current in s:
            both = current + prev
            prev = ""
            if both in comb:
                final[-1:] = comb[both]
            elif current in opp and opp[current] in final:
                final = []
            else:
                final += current
                prev = current

        final_s = "[" + ", ".join(final) + "]"
        print >>out, "Case #%d: %s" % (i, final_s)

    inp.close()
    out.close()

if __name__ == "__main__":
    main()
