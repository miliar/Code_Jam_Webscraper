
file_in = open('a.in', 'r')
file_out = open('a.out', 'w')

n_case = int(file_in.readline())

class Board:
    def __init__(self, file):
        self.v = []
        for r in range(4):
            self.v.append([int(s) for s in file.readline().split()])

for i_case in range(n_case):
    row1 = int(file_in.readline())
    board1 = Board(file_in)
    row2 = int(file_in.readline())
    board2 = Board(file_in)
    sol = set(board1.v[row1-1]) & set(board2.v[row2-1])
    out = "Case #" + str(i_case+1) + ": "
    if len(sol) == 1:
        out += str(list(sol)[0])
    elif len(sol) > 1:
        out += "Bad magician!"
    else:
        out += "Volunteer cheated!"
    file_out.write(out + "\n")

file_in.close()
file_out.close()
