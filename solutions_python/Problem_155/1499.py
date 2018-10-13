import sys

output_line = "Case #{X:d}: {num_friends:d}"


if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            max_shy, audience = inhandle.readline().split()

            people = 0
            num_friends = 0
            for required, count in enumerate(audience):
                if required > people:
                    num_friends += required - people
                    people += required - people
                people += int(count)

            outline = output_line.format(X=t + 1, num_friends=num_friends)
            print(outline, file=outhandle)
            print(outline)
