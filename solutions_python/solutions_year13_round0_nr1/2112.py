file_in = open('A-large.in', 'r')
file_out = open('tictac.out', 'w')
N = int(file_in.readline())

class TestCase:
    def __init__(self):
        self.row_l = []
        self.column_l = []
        self.diag_l = []

    def compute_rows(self, line_l):
        for i in range(4):
            self.row_l.append(line_l[i])
        print self.row_l

    def compute_columns(self, line_l):
        for i in range(4):
            col = ""
            for j in range(4):
                col += line_l[j][i]
            self.column_l.append(col)
        print self.column_l

    def compute_diags(self, line_l):
        diag0 = ""
        diag1 = ""
        for i in range(4):
            for j in range(4):
                if i == j:
                    diag0 += line_l[j][i]
                if i == 3 - j:
                    diag1 += line_l[i][j]
        self.diag_l.append(diag0)
        self.diag_l.append(diag1)
        print self.diag_l

    def check_winner(self, line_l):
        for line in line_l:
            if line.count("X") == 3 and line.count("T") == 1 or \
               line.count("X") == 4:
                return "X"
            elif line.count("O") == 3 and line.count("T") == 1 or \
                 line.count("O") == 4:
                return "O"
        return None

    def check_winner_all(self):
        winner = self.check_winner(self.row_l)
        if winner is not None:
            return winner

        winner = self.check_winner(self.column_l)
        if winner is not None:
            return winner

        winner = self.check_winner(self.diag_l)
        if winner is not None:
            return winner

        return None

    def compute_output(self, test_id):
        # Check for winners:
        winner = self.check_winner_all()

        if winner == None:
            # Check Draw => No empty square
            draw = True
            for row in self.row_l:
                if "." in row:
                    draw = False
            if not draw:
                result = "Game has not completed"
            else:
                result = "Draw"
        else:
            result = "%s won" % winner

        output = "Case #%d: %s\n" % (test_id, result)
        file_out.write(output)


test_l = []
for i in range(N):
    test_l.append(TestCase())
    line_l = []
    for j in range(4):
        line_l.append(file_in.readline().rstrip("\n"))

    test_l[i].compute_rows(line_l)
    test_l[i].compute_columns(line_l)
    test_l[i].compute_diags(line_l)
    test_l[i].compute_output(i+1)
    dummy = file_in.readline()
    print ""
    #test[i].compute_diag(line_l)


    #    test.row.append(file_in.readline())
    #test[i].roa = int(file_in.readline())
    #test[i].I = int(file_in.readline())
    #test[i].P = file_in.readline().rstrip("\n").split(" ")
    #print test[i]
