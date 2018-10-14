import sys

file = sys.argv[1]
print(file)


def main():
    with open(file, 'r') as i:
        with open(file + " out", 'w') as o:
            for i, line in enumerate(i):
                if i > 0:
                    o.write("Case #{}: {}\n".format(i, prog(list(str(line.strip())))))

def prog(arg):
    arg = [int(v) for v in arg]

    for i in range(1, len(arg)):
        if arg[-i] < arg[-i-1]:
            arg[-i-1] -= 1
            for j in range(1, i + 1):
                arg[-j] = 9

    arg = [str(v) for v in arg]
    arg = "".join(arg)
    arg = int(arg)

    return arg


if __name__ == "__main__":
    main()
