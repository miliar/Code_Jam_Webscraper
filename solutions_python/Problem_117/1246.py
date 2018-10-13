__author__ = 'joranvar'
__problem__ = 'B'

class Field(object):
    def __init__(self, data, height, width):
        self.data = data
        self.height = height
        self.width = width

    def is_cuttable(self):
        max_x = [max([self.data[y][x] for x in range(self.width)]) for y in range(self.height)]
        max_y = [max([self.data[y][x] for y in range(self.height)]) for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                if self.data[y][x] < min(max_x[y], max_y[x]):
                    return False
        return True

def read_field(f_in, width, height):
    field_data = [[int(square) for square in f_in.readline().split()] for line in range(height)]
    field = Field(field_data, height, width)
    return field

def solve(case, f_in):
    N, M = list(map(int, f_in.readline().split()))
    field = read_field(f_in, M, N)
    if field.is_cuttable(): return ['Case #{}: YES\n'.format(case + 1)]
    return ['Case #{}: NO\n'.format(case + 1)]


def open_last_file():
    for problem_type in ['-large', '-small-attempt1', '-sample']:
        try:
            return problem_type, open(__problem__ + problem_type + '.in', 'r')
        except FileNotFoundError:
            pass

    raise FileNotFoundError("No input file found!")

if __name__ == '__main__':
    problem_type, f_in = open_last_file()
    print (problem_type)
    f_out = open(__problem__ + problem_type + '.out', 'w')

    T = int(f_in.readline())
    for case in range(T):
        f_out.writelines(solve(case, f_in))
