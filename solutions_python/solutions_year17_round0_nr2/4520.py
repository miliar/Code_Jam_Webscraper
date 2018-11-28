import sys

def main():
    lines = sys.stdin.read().split("\n")
    for casenum, line in enumerate(lines[1:]):
        if len(line) == 0:
            continue

        out = []
        broke = False
        for i in range(len(line[:-1])):
            if not broke:
                if line[i] > line[i+1]:
                    broke = True
                    new = chr(ord(line[i]) - 1)
                    out.append(new)
                    for j in range(len(out) - 1):
                        if out[-j] > new:
                            out[-j + 1] = "9"
                            out[-j] = new
                else:
                    out.append(line[i])
            else:
                out.append("9")

        if broke:
            out.append("9")
        else:
            out.append(line[-1])

        print "Case  #{}: {}".format(casenum + 1, int("".join(out)))

if __name__ == "__main__":
    main()
