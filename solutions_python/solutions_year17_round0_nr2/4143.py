import sys
import functools


@functools.lru_cache(maxsize=None)
def lastTidy(n):
    i = 0
    while i < len(n) - 1 and n[i] <= n[i + 1]:
        i += 1

    if i == len(n) - 1:
        return n
    else:
        return lastTidy(n[:i] + (n[i] - 1,) + tuple(9 for _ in range(i + 1, len(n))))


def lastTidyInt(n):
    return int("".join(map(str, lastTidy(tuple(map(int, str(n)))))))

# print(lastTidyInt(111111111111111110))
if __name__ == '__main__':
    inputFileName = sys.argv[1]
    outputFileName = inputFileName.replace(".in", ".out")

    with open(inputFileName, "r") as file:
        lines = file.readlines()

    T = int(lines[0])
    N = [int(e) for e in lines[1:]]

    with open(outputFileName, "w") as file:
        file.write(
            "\n".join("Case #{}: {}".format(i + 1, lastTidyInt(int(n))) for i, n in enumerate(N))
            + "\n"
        )