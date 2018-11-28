import sys


def main():
    with open(sys.argv[1], "r", encoding="ascii") as a_file, \
            open(sys.argv[1] + "_output", "w", encoding="ascii") as out_file:
        test_cases = int(a_file.readline())
        for test_case in range(test_cases):
            s = a_file.readline().strip()
            if len(s) == 1:
                out_file.write("Case #%d: %s\n" % (test_case+1, s))
            dt = ""
            count = 0
            for let in s:
                count += 1
                if len(dt) == 0:
                    dt = let
                else:
                    dt = max([dt + let, let + dt])
                    if count == len(s):
                        out_file.write("Case #%d: %s\n" % (test_case+1, dt))

            print(dt)
            #


if __name__ == "__main__":
    main()
