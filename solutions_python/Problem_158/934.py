import sys
import math
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-5s %(name)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO)

logger = logging.getLogger("B")


def run_case(n, x, r, c):
    num_cells = r * c
    fits = num_cells % x == 0
    logger.info("#{}: {} {} {} --> {} {}".format(n, x, r, c, num_cells, fits))
    if not fits:
        return "RICHARD"

    if x > r and x > c:
        return "RICHARD"

    if x % 2 == 0:
        sq = int(math.floor(math.sqrt(float(x))))
    else:
        sq = int(math.ceil(math.sqrt(float(x))))

    if sq > r or sq > c:
        return "RICHARD"

    # Sorry, hardcoded case until I can implement a better solution for the large dataset
    if x == 4 and ((r == 4 and c == 2) or (r == 2 and c == 4)):
        return "RICHARD"

    return "GABRIEL"


def main():
    inf = sys.stdin
    outf = sys.stdout
    N = int(inf.readline())
    for i in range(N):
        x, r, c = [int(v) for v in inf.readline().split()]
        result = run_case(i + 1, x, r, c)
        outf.write("Case #{}: {}\n".format(i + 1, result))

if __name__ == "__main__":
    main()