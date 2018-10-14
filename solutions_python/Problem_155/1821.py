#! python3

def main():
    with open("A-large.in") as in_file:
        with open("A-large.out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '').split(' ')
                max_shyness = int(line[0])
                audience = line[1]
                missing = 0
                total = 0

                for y in range(max_shyness):
                    member = audience[y]
                    total += int(member)
                    if total < y + 1:
                        missing += 1
                        total += 1

                fout.write("Case #{0}: {1}\n".format(x + 1, missing))

if __name__ == "__main__":
    main()
