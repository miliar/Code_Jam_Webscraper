import utils

# Custom functions
def flip(row, index, flipSize):
    count = 0
    str = "";

    for i in range(0, len(row)):
        if i < index or i >= index + flipSize:
            str += row[i]
        else:
            if (row[i] == '+'):
                str += '-'
            else:
                str += '+'

    return str

def check(row):
    for i in range(0, len(row)):
        if row[i] == '-':
            return False

    return True

# Base functions
def case(line):
    row, flipSize = line.split(' ')
    flipSize = int(flipSize)

    flips = 0

    for i in range(0, len(row) - flipSize + 1):
        if (row[i] == '-'):
            row = flip(row, i, flipSize)
            flips += 1

    return [check(row), flips]

def main():
    lines = utils.readFile("test")
    i = 1;
    result = []

    for line in lines:
        c, flips = case(line)

        if c:
            print("Case #" + str(i) + ": " + str(flips))
            result.append("Case #" + str(i) + ": " + str(flips))
        else:
            print("Case #" + str(i) + ": IMPOSSIBLE")
            result.append("Case #" + str(i) + ": IMPOSSIBLE")

        i += 1

    utils.saveToFile('result', result)

if __name__ == "__main__":
    main();