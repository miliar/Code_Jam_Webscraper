#!/usr/bin/env python3

class Pankakes:
    def __init__(self, start, flipper_width=4):
        self.start = start
        self.flipper_width = flipper_width
        self.nodes = {start: 0}

    @staticmethod
    def flip(pankakes, k, x):
        pankakes = list(pankakes)
        for i in range(k):
            pankakes[i + x] = '+' if pankakes[i + x] == '-' else '-'
        return ''.join(pankakes)

    def create_graph(self, pankakes=None, distance=1):
        pankakes = self.start if pankakes is None else pankakes
        qty_pankakes = len(self.start)
        for i in range(0, qty_pankakes - self.flipper_width + 1):
            new_node = Pankakes.flip(pankakes, self.flipper_width, i)
            if new_node not in self.nodes:
                self.nodes[new_node] = distance
                self.create_graph(new_node, distance + 1)
            else:
                if distance < self.nodes[new_node]:
                    self.nodes[new_node] = distance
                    self.create_graph(new_node, distance + 1)


def main():
    import sys
    test_cases = None
    case = 1
    with open(sys.argv[1]) as infile:
        for line in infile:
            line = line.strip()
            if test_cases is None:
                test_cases = line
                continue
            pankakes, k = line.split()
            row = Pankakes(pankakes, int(k))
            row.create_graph()
            all_side_up = '+' * len(pankakes)
            if all_side_up in row.nodes:
                print("Case #{}: {}".format(case, row.nodes[all_side_up]))
            else:
                print("Case #{}: IMPOSSIBLE".format(case))
            case += 1


if __name__ == '__main__':
    main()
