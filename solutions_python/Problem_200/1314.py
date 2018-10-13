import sys


def tidy_numbers(path_in, path_out):
    with open(path_in, 'rb') as fin:
        lines = fin.readlines()
    length = int(lines[0].split('\r')[0])
    out = []
    for i in range(1, length + 1):
        out += "Case #" + str(i) + ": "
        n = [int(s) for s in (lines[i].split('\n')[0])]
        for j in range(len(n)-1, 0, -1):
            if n[j-1] > n[j]:
                n[j-1] -= 1
                for k in range(j, len(n)):
                    if n[k] == 9:
                        break
                    n[k] = 9
        if n[0] == 0:
            n = n[1:]
        out += "".join(str(x) for x in n) + "\r\n"
    out = "".join(out[:-2])
    with open(path_out, 'wb') as fout:
        fout.write(out)

if __name__ == "__main__":
    tidy_numbers(sys.argv[1], sys.argv[2])
