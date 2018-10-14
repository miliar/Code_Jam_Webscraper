def solve(d, lines):
    time = None
    for loc, speed in lines:
        if time is None:
            time = (d - loc) / speed
        else:
            time = max((d - loc) / speed, time)

    return d / time


def main():
    input_file_name = 'A-input.in'
    output_file_name = 'A-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for tc in range(t):
                d, n = tuple(map(int, fin.readline().split()))
                lines = []
                for i in range(n):
                    lines.append(list(map(int, fin.readline().split())))
                fout.write("Case #%d: %f\n" % ((tc + 1), solve(d, lines)))
main()