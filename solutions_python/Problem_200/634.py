#! python3

DATA_FILE = "B-large"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                N = int(line)
                N_str = str(N)

                i = 0
                while i < len(N_str) - 1:
                    l = len(N_str) - 1
                    curr = int(N_str[l - i])
                    left = int(N_str[l - i - 1])
                    if curr < left:
                        N -= int(N_str[l - i:]) + 1
                        N_str = str(N)
                    i += 1

                fout.write("Case #{0}: {1}\n".format(x + 1, N))

if __name__ == "__main__":
    main()
