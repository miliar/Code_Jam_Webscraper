import logging
from math import pi


log = logging.getLogger(__name__)


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


class Pancake:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.top = pi * (radius ** 2)
        self.side = 2.0 * pi * radius * height

    @property
    def total_surface(self):
        return self.top + self.side


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d - %(message)s",
        datefmt="%H:%M:%S"
    )

    log.info("Started")

    n_cases = read_int()
    for c in range(n_cases):
        pancakes = []
        n_pancakes, stack_size = read_ints()
        for p in range(n_pancakes):
            radius, height = read_ints()
            pancakes.append(Pancake(radius, height))

        if stack_size > 1:
            s_pancakes = list(sorted(pancakes, key=lambda p: p.side, reverse=True))
            stack = s_pancakes[:stack_size - 1]
            pancakes = s_pancakes[stack_size - 1:]

            max_stack_top = max(p.top for p in stack)
            candidates = filter(lambda p: p.top >= max_stack_top, pancakes)
            candidate = max(candidates, key=lambda p: p.side + (p.top - max_stack_top), default=None)



            if candidate and candidate.side + (candidate.top - max_stack_top) > pancakes[0].side:
                stack.append(candidate)
            else:
                stack = s_pancakes[:stack_size]
        else:
            stack = [max(pancakes, key=lambda p: p.total_surface)]


        total = sum(p.side for p in stack)
        total += max(p.top for p in stack)

        print("Case #%d: %.9f" % (c+1, total))

    log.info("Done")


if __name__ == '__main__':
    main()
