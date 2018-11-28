import sys

def candy_splitting(values):
    test = 0
    for value in values:
        test = test ^ value
    if test != 0: return "NO"
    return str(sum(sorted(values)[1:]))

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(int(Input[0])):
        values = Input[2*i + 2].split(' ')
        values = [int(value) for value in values]
        result = candy_splitting(values)
        Output += "Case #" + str(i + 1) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__":
    main(sys.argv[1])
