import sys

def find_tidy(last):
    """Find largest tidy number smaller than n."""
    n = last
    while True:
        digits = list(map(int, str(n)))
        # find first digits that is "wrong"
        for i in range(len(digits) - 1):
            if digits[i] > digits[i + 1]:
                # digits below i'th one
                skip = n % (10 ** (len(digits) - 1 - i))
                break
        else:
            # found the first (and largest) tidy number!
            return n

        # n wasn't a tidy one, but we can skip a few checks
        n -= (skip + 1)

def main():
    # read data
    filename = sys.argv[-1]
    with open(filename, "r") as f:
        last_n = list(map(int, f.readlines()[1:]))

    with open("output.txt", "w") as output:
        for i, n in enumerate(last_n):
            print("Case #{}: {}".format(i + 1, find_tidy(n)), file=output)

if __name__ == "__main__": main()
