# Coded by Jeff Garcia (may god have mercy on my soul)

def main():
    output_file = open("/home/koofu/PycharmProjects/CodeJam/large_output.out", 'w')

    with open("/home/koofu/PycharmProjects/CodeJam/B-large.in", 'r') as f:
        test_cases = f.readline().strip()
        for counter, rawline in enumerate(f):
            if counter+1 > int(test_cases):
                break
            line = rawline.strip()
            output_file.write("Case #{0}: {1}".format(counter+1, solve(line)+'\n'))


def solve(stripped_line):
    for index, character in enumerate(stripped_line):
        if index+1 >= len(stripped_line):
            return stripped_line
        elif int(character) > int(stripped_line[index + 1]):
            if character == "1":
                return solve("".ljust(len(stripped_line) - 1, '9'))
            else:
                return solve(stripped_line[0:index] + str(int(character) - 1) + "".ljust(len(stripped_line)
                                                                                         - (index + 1), '9'))

if __name__ == "__main__":
    main()
