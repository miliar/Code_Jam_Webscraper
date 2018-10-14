class PancakeSolver(object):
    def __init__(self, size):
        self.steps = []
        self.size = size

    def has_been_tried(self, state):
        str_state = ''.join(state)
        for step in self.steps:
            if ''.join(step) == str_state:
                return True
        return False

    @staticmethod
    def is_valid(state):
        return all(pancake == '+' for pancake in state)

    def flip(self, state, start):
        result = state[:]
        for i in range(start, start + self.size):
            result[i] = self.switch(result[i])
        return result

    @staticmethod
    def switch(pancake):
        if pancake == '+':
            return '-'
        return '+'

    def next_states(self, state, skip):
        result = []
        for start_point in range(0, len(state) - self.size + 1):
            partial = self.flip(state, start_point)
            total_partial = ['+' for _ in range(0, skip)]
            total_partial.extend(partial)
            if not self.has_been_tried(total_partial):
                result.append(total_partial)
                self.steps.append(total_partial)
        return result

    def solve(self, state):
        if self.is_valid(state):
            # print(state)
            return True, 0
        else:
            min_start = state.index('-')
            if len(state) - min_start < self.size:
                min_start = len(state) - self.size
            max_val = min_start - self.size + 1
            if max_val < 0:
                max_val = 0
            min_steps = None
            # previous_tested = self.steps[:]
            while min_start >= max_val:
                # self.steps = previous_tested[:]
                possibilities = self.next_states(state[min_start:], min_start)
                for possibility in possibilities:
                    solved, steps = self.solve(possibility)
                    if solved:
                        # print(state)
                        if min_steps is None or min_steps > steps:
                            min_steps = steps
                if min_steps is not None:
                    # print(state)
                    return True, min_steps + 1

                min_start -= 1
            return False, 'IMPOSSIBLE   '


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in range(0, t):
        state, size = raw_input().split(" ")
        state = list(state)
        solver = PancakeSolver(size=int(size))
        solved, steps = solver.solve(state)
        print ('Case #{}: {}'.format(i + 1, steps))


def fashion():
    t = int(raw_input())
    for i in range(1, t + 1):
        grid_size, original_models = [int(x) for x in raw_input().split(" ")]
        grid = [['.' for _ in range(0, grid_size)] for _ in range(0, grid_size)]
        for _ in range(0, original_models):
            model, x, y = raw_input().split(" ")
            grid[int(x) - 1][int(y) - 1] = model
        for row in grid:
            print("".join(row))

if __name__ == '__main__':
    # import sys
    # sys.setrecursionlimit(25000)
    main()
