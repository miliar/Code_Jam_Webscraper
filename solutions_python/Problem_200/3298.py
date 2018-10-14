import os


def reader(file):
    f_out = file[:-2] + "out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            line = f.readline()
            solver(t, line, f_out)


def solver(t, line, f_out):
    if is_number_tidy(line):
        solution = line
    else:
        n = int(line)
        while not is_number_tidy(str(n)):
            n -= 1
        solution = n
    with open(f_out, 'a') as f:
        f.write("Case #{}: {}\n".format(t + 1, solution))


def is_number_tidy(number):
    """ number is type: string """
    for i in range(len(number)-1):
        if number[i] > number[i + 1]:
            return False
    return True


def main():
    reader('B-small.in')

main()
