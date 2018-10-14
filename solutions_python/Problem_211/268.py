import logging


log = logging.getLogger(__name__)


def read_int():
    return int(input())


def read_float():
    return float(input())


def read_ints():
    return tuple(map(int, input().split()))

def read_floats():
    return tuple(map(float, input().split()))


class Core:
    def __init__(self, p):
        self.p = p


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d - %(message)s",
        datefmt="%H:%M:%S"
    )

    log.info("Started")

    n_cases = read_int()
    for case in range(n_cases):
        n_cores, n_success = read_ints()
        units = read_float()
        cores = [Core(p) for p in read_floats()]

        while units > 0:
            min_p = min(c.p for c in cores)
            min_cores = list(filter(lambda c: c.p == min_p, cores))

            next_min_p = min((c.p for c in filter(lambda c: c.p > min_p, cores)), default=None)

            if next_min_p is None or units <= (next_min_p - min_p) * len(min_cores):
                for c in min_cores:
                    c.p += (units / len(min_cores))
                break
            else:
                diff = next_min_p - min_p
                for c in min_cores:
                    c.p += diff
                units -= (diff * len(min_cores))

        res = 1
        for core in cores:
            res *= core.p

        print("Case #%d: %.6f" % (case+1, res))

    log.info("Done")


if __name__ == '__main__':
    main()
