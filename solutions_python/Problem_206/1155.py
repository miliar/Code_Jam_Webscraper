import sys


def a(path_in, path_out):
    with open(path_in, 'rb') as fin:
        lines = fin.readlines()
    length = int(str.strip(lines[0]))
    out = []
    lineind = 1
    for i in range(1, length + 1):
        out += "Case #" + str(i) + ": "
        line = str.strip(lines[lineind])
        splitted = line.split(' ')
        d = float(splitted[0])
        n = int(splitted[1])
        maxt = 0
        for j in range(1, n+1):
            line = str.strip(lines[lineind + j])
            splitted = line.split(' ')
            k = float(splitted[0])
            s = float(splitted[1])
            t = (d - k)/s
            maxt = max(t, maxt)
        out += str(d/maxt) +"\r\n"
        lineind += n + 1
    out = "".join(out[:-2])
    with open(path_out, 'wb') as fout:
        fout.write(out)

if __name__ == "__main__":
    a(sys.argv[1], sys.argv[2])
