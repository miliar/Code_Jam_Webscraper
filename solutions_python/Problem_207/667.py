#!/usr/local/bin/python3

import logging


def solve(problem):
    N, R, O, Y, G, B, V = problem
    from collections import Counter

    opposite_colors = {
        "R" : ["Y", "G", "B"],
        "O" : ["G", "B", "V"],
        "Y" : ["B", "V", "R"],
        "G" : ["V", "R", "O"],
        "B" : ["R", "O", "Y"],
        "V" : ["O", "Y", "G"],
    }

    def deficit(color, counter):
        return sum(counter[c] for c in opposite_colors[color]) - counter[color]

    def extend(solution, node):
        if node is None:
            counter = Counter({
                "R" : R,
                "O" : O,
                "Y" : Y,
                "G" : G,
                "B" : B,
                "V" : V,
            })
            colors = [c for c in counter.keys() if deficit(c, counter) >= 0]
        else:
            c, counter = node
            colors = opposite_colors[c]
        options = []
        for color in colors:
            if counter[color] == 0:
                continue
            counter_ = Counter(counter)
            counter_[color] -= 1
            option = (color, counter_)
            options.append(option)
        options.sort(key=lambda option: counter[option[0]])
        return iter(options)

    def present(solution):
        return "".join(color for (color, counter) in solution)

    def accept(solution, node):
        return len(solution) == N

    def reject(solution, node):
        assert not node is None
        if len(solution) == N:
            c0, _ = solution[0]
            cN, _ = solution[-1]
            return not c0 in opposite_colors[cN]
        c, counter = node
        return deficit(c, counter) < 0

    def backtrack():
        solution = []
        options = [extend(solution, None)]
        while True:
            try:
                node = next(options[-1])
                solution.append(node)
                if reject(solution, node):
                    solution.pop()
                    continue
                if accept(solution, node):
                    yield present(solution)
                it = extend(solution, node)
                if not it is None:
                    options.append(it)
                else:
                    solution.pop()
            except StopIteration:
                options.pop()
                if not options:
                    return
                solution.pop()

    for s in backtrack():
        return s
    return "IMPOSSIBLE"

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        yield tuple(map(int, next(fin).split()))

def main():
    import time
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    t0 = time.time()
    logging.info("Starting...")
    for i, p in enumerate(parse_problems()):
        ans = solve(p)
        logging.info("Solved #%d", i + 1)
        print("Case #{}: {}".format(i + 1, ans))
    logging.info("Finished in %.2f s", time.time() - t0)

if __name__ == '__main__':
    main()
