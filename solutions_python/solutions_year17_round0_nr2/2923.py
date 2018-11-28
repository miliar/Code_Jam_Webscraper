def is_tidy(num):
    lst = []
    num_str = str(num)
    prev = 1
    for ch in num_str:
        digit = int(ch)
        if digit >= prev:
            prev = digit
            continue
        return False
    return True

def read_file():
    file = open('input.file', 'r')
    lines = file.readlines()
    lines = list(map(int, lines))

    return lines

def find_last_tidy(n):
    for i in range(n,0,-1):
        if is_tidy(i):
            return i


def main():
    lines = read_file()
    cases = lines[0];
    inputs = lines[1:]
    output = ''
    for i in range(len(inputs)):
        output += "Case #{0}: {1}\n".format(i+1,find_last_tidy(inputs[i]))
    output = output[:-1]
    (open('output.file', 'w')).write(output)

main()

