import sys


def turn(sequence, start, length):
    for i in range(start, start + length):
        if sequence[i] == "-":
            sequence[i] = "+"
        else:
            sequence[i] = "-"


def flip(input, case):
    sequence, length = input.split(" ")
    sequence = list(sequence)
    length = int(length)
    flips = 0

    for i in range(0, len(sequence)-length+1):
        if sequence[i] == "-":
            flips += 1
            turn(sequence, i, length)

    for i in range(len(sequence)-length+1, len(sequence)):
        if sequence[i] == "-":
            return "Case #" + str(case) + ": IMPOSSIBLE\n"

    return "Case #" + str(case) + ": " + str(flips) + "\n"


def pancake(input, output):
    # Read input
    with open(output, "w") as o:
        with open(input, "r") as f:
            f.readline() # Read number of examples
            # Process examples
            i = 1
            for line in f:
                o.write(flip(line, i))
                i += 1


if __name__ == '__main__':
    pancake(sys.argv[1], sys.argv[2])
