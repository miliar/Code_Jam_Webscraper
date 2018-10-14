
def main(line):
    line = [int(c) for c in str(line[:-1])]
    line_num = len(line)
    for idx, num in reversed(list(enumerate(line[:-1]))):
        if num > line[idx + 1]:
            line[idx] = num - 1
            for i in range(idx + 1, line_num):
                line[i] = 9
    return int(''.join([str(c) for c in line]))


if __name__ == '__main__':
    with open('B-small.out', 'w') as outfile:
        with open('B-small.in', 'r') as file:
            count = int(file.readline())
            for idx in range(1, count + 1):
                line = file.readline()
                outfile.write("Case #{}: {}\n".format(idx, main(line)))


            