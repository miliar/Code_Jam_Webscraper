import sys
import numpy as np
import math

file = sys.argv[1]
print(file)


def main():
    with open(file, 'r') as i:
        with open(file + " out", 'w') as o:
            for i, line in enumerate(i):
                if i > 0:
                    res = prog([int(v) for v in line.strip().split(" ")])
                    o.write("Case #{}: {} {}\n".format(i, res[0], res[1]))

def prog(arg):
    stalls = np.array([arg[0]])
    for i in range(arg[1]):
        ind = np.argmax(stalls)
        val = stalls[ind]

        midl = math.floor((val - 1) / 2)
        midr = math.floor(val / 2)

        if int(midr) == 0:
            stalls = np.delete(stalls, ind)

        else:
            stalls[ind] = int(midr)
            if midl > 0:
                stalls = np.insert(stalls, ind, int(midl))

    return midr, midl


if __name__ == "__main__":
    main()
