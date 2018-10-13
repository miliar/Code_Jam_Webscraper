def istidy(n):
    s = str(n)
    if len(s) == 1:
        return True
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i - 1]):
            return False
    return True


def nearest_tidy(n):
    for i in range(n, 0, -1):
        if istidy(i):
            return i

if __name__ == '__main__':
    with open('B-small-attempt0.in', 'r') as f:
        lines = f.readlines()
    numcases = int(lines[0].strip())
    with open('outputs.txt', 'w') as f:
        for linenum, line in enumerate(lines[1:]):
            near_tidy = nearest_tidy(int(line.strip()))
            out_line = 'Case #{0}: {1}\n'.format(linenum + 1, near_tidy)
            f.write(out_line)
