import logging


log = logging.getLogger(__name__)


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d - %(message)s",
        datefmt="%H:%M:%S"
    )

    log.info("Started")

    n_cases = read_int()
    for c in range(n_cases):
        destination, n_horses = read_ints()
        durations = []
        for h in range(n_horses):
            position, speed = read_ints()
            durations.append(
                (destination - position) / float(speed)
            )
        speed = destination / max(durations)
        print("Case #%d: %.6f" % (c+1, speed))

        log.info("%s", speed)

    log.info("Done")


if __name__ == '__main__':
    main()
