import sys

__author__ = 'laurens'


class Linear:
    def __init__(self, a, offset):
        self.a = a
        self.offset = offset

    def solve_x_for_y(self, y):
        return self.offset + (y / self.a)


class LinearSystem:
    def __init__(self, costs, production, goal):
        self.base_prod = 2
        self.costs = costs
        self.production = production
        self.goal = goal

    def solve(self):
        first = Linear(self.base_prod, 0)
        second = Linear(self.base_prod + self.production, first.solve_x_for_y(self.costs))

        while first.solve_x_for_y(self.goal) > second.solve_x_for_y(self.goal):
            first = second
            second = Linear(first.a + self.production, first.solve_x_for_y(self.costs))

        return first.solve_x_for_y(self.goal)


file_in = open(sys.argv[1], 'r')
file_out = open(sys.argv[2], 'w')

tests = int(file_in.readline())

for x in range(0, tests):
    costs, production, goal = [float(x) for x in file_in.readline().split()]

    system = LinearSystem(costs, production, goal)

    file_out.write(('Case #' + str(x + 1) + ': ' + str(system.solve()) + '\n'))