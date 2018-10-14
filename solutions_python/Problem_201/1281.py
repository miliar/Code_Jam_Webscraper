import sys
import math


def rec(n, k):
    if k == 1:
        return n
    div = (n-1)/2
    if k % 2 == 1:
        return rec(math.floor(div), int(k/2))
    else:
        return rec(math.ceil(div), int(k/2))


def bathroom_stalls(path_in, path_out):
    with open(path_in, 'rb') as fin:
        lines = fin.readlines()
    length = int(lines[0].split('\r')[0])
    out = []
    for i in range(1, length + 1):
        out += "Case #" + str(i) + ": "
        line = lines[i].split(' ')
        n = int(line[0].strip())
        k = int(line[1].strip())
        ans = rec(float(n), k)
        print ans
        div = (ans-1)/2
        print div
        out += str(int(math.ceil(div))) + " " + str(max(0, int(math.floor(div)))) + "\r\n"
    out = "".join(out[:-2])
    print out
    with open(path_out, 'wb') as fout:
        fout.write(out)

if __name__ == "__main__":
    bathroom_stalls(sys.argv[1], sys.argv[2])
