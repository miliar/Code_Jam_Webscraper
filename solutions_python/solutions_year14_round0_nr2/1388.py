__author__ = 'nik'


def main():
    output_file = open('output', 'w')
    with open('input') as input_file:
        next(input_file)
        case_num = 0
        for line in input_file:
            if line.endswith('\n'):
                line = line[: len(line) - 1]
            line = line.split(' ')

            s = 2
            time = 0
            c = float(line[0])
            f = float(line[1])
            x = float(line[2])

            while (x / s) > (x / (s + f) + (c / s)):
                time += c / s
                s += f
            else:
                time += x / s

            case_num += 1

            out = "Case #" + str(case_num) + ": " + "{0:.7f}".format(time) + "\n"
            output_file.write(out)
            print(out)


if __name__ == '__main__': main()