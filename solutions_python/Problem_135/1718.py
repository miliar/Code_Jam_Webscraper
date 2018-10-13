class Solver(object):
    def __init__(self, rows_picked, arrangements):
        self.rows_picked = rows_picked
        self.arrangements = arrangements

    def solve(self):
        first_row = self.arrangements[0][4*self.rows_picked[0]-4:4*self.rows_picked[0]]
        second_row = self.arrangements[1][4*self.rows_picked[1]-4:4*self.rows_picked[1]]

        # find intersection
        intersection = []
        for i in first_row:
            if i in second_row:
                intersection.append(i)

        if len(intersection) == 0:
            return "Volunteer cheated!"
        elif len(intersection) > 1:
            return "Bad magician!"
        else:
            return intersection[0]

f = open('test.txt')
num_cases = int(f.readline())

out = open('out.txt', 'w')

for i in range(num_cases):
    rows_picked = []
    arrangements = []
    for _ in range(2):
        rows_picked.append(int(f.readline()))
        arrangement = []
        for _ in range(4):
            for n in f.readline().strip().split(' '):
                arrangement.append(int(n))
        arrangements.append(arrangement)
    s = Solver(rows_picked, arrangements)
    # print s.solve()
    out.write("Case #%d: %s\n" % (i+1, s.solve()))