class UnicornProblem:

    def __init__(self, r, o, y, g, b, v):
        self.r = r
        self.y = y
        self.b = b
        self.o = o
        self.g = g
        self.v = v
        self.total = r + y + b + o + g + v

    def output_with_only_r_y_b(self):
        output_set = {
            "R": self.r,
            "Y": self.y,
            "B": self.b,
        }
        output_set = self.remove_zeros(output_set)
        last_output = ""
        output_string = ""
        first_colour = ""
        try:
            while output_set:
                k = self.sorted_keys(output_set, first_colour)
                next_output = next(x for x in k if x != last_output)
                output_string += next_output
                last_output = next_output
                output_set[next_output] -= 1
                if output_set[next_output] == 0:
                    del output_set[next_output]
                first_colour = output_string[0]
            assert output_string[0] != output_string[-1]
            return output_string
        except:
            return "IMPOSSIBLE"

    @staticmethod
    def sorted_keys(d, first_colour):
        items = [(k, v) for k, v in d.items()]
        sorted_items = sorted(
            items,
            # In a tie break, pick the colour of the starting horse first
            key=lambda x: x[1] + 0.5 if first_colour == x[0] else x[1],
            reverse=True
        )
        return map(lambda x: x[0], sorted_items)

    @staticmethod
    def remove_zeros(d):
        return {k: v for k, v in d.items() if v != 0}


num_cases = int(input())
for i in range(1, num_cases + 1):
    n, r, o, y, g, b, v = [int(x) for x in input().split(" ")]
    problem = UnicornProblem(r, o, y, g, b, v)
    print("Case #{}: {}".format(i, problem.output_with_only_r_y_b()))
