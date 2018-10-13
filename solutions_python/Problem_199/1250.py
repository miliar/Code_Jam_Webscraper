import sys


def oversized_pancake_flipper(path_in, path_out):
    with open(path_in, 'rb') as f:
        lines = f.readlines()
    length = int(lines[0].split('\r')[0])
    out = []
    for i in range(1, length + 1):
        out += "Case #" + str(i) + ": "
        line = lines[i].split(' ')
        arr = list(line[0])
        k = int(line[1].split('\r')[0])
        flips = 0
        for j in range(len(arr) - k + 1):
            if arr[j] == '-':
                flips += 1
                for l in range(k):
                    if arr[j + l] == '+':
                        arr[j + l] = '-'
                    else:
                        arr[j + l] = '+'
        if "".join(arr[-k:]) != '+' * k:
            out += "IMPOSSIBLE\r\n"
        else:
            out += str(flips) + "\r\n"
    out = "".join(out[:-2])
    with open(path_out, 'wb') as fout:
        fout.write(out)


if __name__ == "__main__":
    oversized_pancake_flipper(sys.argv[1], sys.argv[2])
