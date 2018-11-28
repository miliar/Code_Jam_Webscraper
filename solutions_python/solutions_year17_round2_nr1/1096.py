# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


def main():
    t = int(input())  # read a line with a single integer

    for tt in range(1, t + 1):
        d, n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        s = None
        for __ in range(n):
            ki, si = [int(s) for s in input().split(" ")]
            new_s = d * si / (d - ki)
            if not s:
                s = new_s
            else:
                s = min(s, new_s)
        print("Case #{}: {:.10f}".format(tt, s))


if __name__ == "__main__":
    main()
