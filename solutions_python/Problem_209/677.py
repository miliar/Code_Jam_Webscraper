import math


class Pancake:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        return "Pancake(radius=%s, height=%s)" % (self.radius, self.height)

class AmpleSyrup:
    @staticmethod
    def get_first_pancake_surface(pancake):
        # return math.pi * (radius ** 2) + 2 * math.pi * radius * height
        return math.pi * pancake.radius * (pancake.radius + 2 * pancake.height)

    @staticmethod
    def get_second_pancake_surface(pancake):
        # return math.pi * (radius ** 2) + 2 * math.pi * radius * height
        return 2 * math.pi * pancake.radius * pancake.height

    @staticmethod
    def solve(n, k, pancakes):
        pancakes = sorted(pancakes, key=lambda x: -x.radius)

        def inner(k, last_stacked, surface, iter):
            # print(k, last_stacked, surface, iter)
            if k == 0 or iter == n:
                return surface
            if last_stacked is None:
                return max(
                    inner(k - 1, pancakes[iter], surface+AmpleSyrup.get_first_pancake_surface(pancakes[iter]), iter+1),
                    inner(k, None, surface, iter+1)
                )

            return max(
                inner(k - 1, pancakes[iter], surface+AmpleSyrup.get_second_pancake_surface(pancakes[iter]), iter + 1),
                inner(k, last_stacked, surface, iter+1)
            )
        return inner(k, None, 0, 0)

    @staticmethod
    def main():
        t = int(input())

        for i in range(0, t):
            line = input()
            n, k = [int(x) for x in line.split(" ")]
            pancakes = []
            for j in range(0, n):
                line = input()
                radius, height = [int(x) for x in line.split(" ")]
                pancakes.append(Pancake(radius, height))
            print('Case #%s: %s' % (i + 1, AmpleSyrup.solve(n, k, pancakes)))

if __name__ == "__main__":
    AmpleSyrup.main()
