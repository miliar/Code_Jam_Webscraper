"""
Problem B

@author: Krisztian Balog
"""


def tidy_violated(n):
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            return i
    return -1

def tidy(n):
    """Takes a string as parameter."""
    tv = tidy_violated(n)
    if tv < 0:  # n is tidy
        return n
    else:
        # tv is the index where tidyness is violated
        # return the biggest number that is the same as n until [0..tv-1], then the closest number to the rest
        tn = n[:tv] if tv > 0 else ""
        tn += str(int(n[tv]) - 1) + "".join(["9"] * (len(n) - 1 - tv))
        # remove leading zeros
        while tn[0] == "0":
            tn = tn[1:]
        return tidy(tn)


def run(infile, outfile):
    with open(infile, "r") as f:
        t = int(f.readline().strip())
        cases = [f.readline().strip() for i in range(t)]
    with open(outfile, "w") as f:
        for i, n in enumerate(cases):
            sol = tidy(n)
            print(sol)
            f.write("Case #" + str(i + 1) + ": " + sol + "\n")


if __name__ == "__main__":
    run("B-large.in", "B-large.out")