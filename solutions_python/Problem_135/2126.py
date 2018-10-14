class Magic(object):
    row1 = 0
    row2 = 0
    grid1 = []
    grid2 = []

    def __init__(self, row1, row2, grid1, grid2):
        self.row1 = row1
        self.row2 = row2
        self.grid1 = grid1
        self.grid2 = grid2


def read_input(file_name):
    magic_list = []
    with open(file_name, 'r') as input_file:
        input_lines = input_file.readlines()
        shows = int(input_lines[0])
        input_lines = input_lines[1:]

    with open('magic_out.txt', 'w+') as output:
        for i in xrange(1, shows + 1):
            # grid1 = [input_lines[1].split(), input_lines[2].split(), input_lines[3], input_lines[4]]
            # magic_show = Magic(int(input_lines[0]), int(input_lines[5]))
            first = set(input_lines[int(input_lines[0])].split())
            second = set(input_lines[int(input_lines[5]) + 5].split())
            intersect = first.intersection(second)


            if len(intersect) > 1:
                output.write("Case #{0}: Bad magician!\n".format(i))
            elif len(intersect) < 1:
                output.write("Case #{0}: Volunteer cheated!\n".format(i))
            else:
                output.write("Case #{0}: {1}\n".format(i, list(intersect)[0]))

            input_lines = input_lines[10:]


if __name__ == '__main__':
    read_input('magic_input.txt')