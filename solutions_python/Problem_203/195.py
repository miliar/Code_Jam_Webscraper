def solve(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = get_char(lines, i, j)
            left = get_char(lines, i, j - 1)
            right = get_char(lines, i, j + 1)

            if is_blank(left):
                index = 1
                while is_blank(get_char(lines, i, j - index)):
                    lines[i][j - index] = current
                    index += 1

            if is_blank(right):
                index = 1
                while is_blank(get_char(lines, i, j + index)):
                    lines[i][j + index] = current
                    index += 1

    for i in range(len(lines)):
        if '?' in lines[i]:
            if i == len(lines) - 1:
                for j in range(len(lines[0])):
                    lines[i][j] = lines[i - 1][j]
            else:
                for l in range(i + 1, len(lines)):
                    if '?' not in lines[l]:
                        for j in range(len(lines[0])):
                            lines[i][j] = lines[l][j]
                        break
                else:
                    for l in range(i, -1, -1):
                        if '?' not in lines[l]:
                            for j in range(len(lines[0])):
                                lines[i][j] = lines[l][j]
                            break





    return "\n".join(map("".join, lines))

def is_blank(c):
    return c is not None and c == '?'

def get_char(lines, i, j):
    if i >= len(lines) or i < 0:
        return None
    if j >= len(lines[0]) or j < 0:
        return None
    return lines[i][j]

def main():
    input_file_name = 'A-input.in'
    output_file_name = 'A-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for tc in range(t):
                r, c = tuple(map(int, fin.readline().split()))
                lines = []
                for i in range(r):
                    lines.append(list(fin.readline().strip()))
                fout.write("Case #%d: \n%s\n" % ((tc + 1), solve(lines)))
main()