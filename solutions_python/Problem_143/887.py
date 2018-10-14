__author__ = 'thomas'


#[]
#{}
#\

class Filehandler():
    def __init__(self, filename=None):
        self.filename = filename
        self.tot_games = None
        self.act_game = 0
        self.f = None
        self.output = None
        _filename = filename + '.out'

    def read_file(self):
        self.f = open(self.filename, 'r')
        self.tot_games = int(self.f.readline())

    def read_single_game(self):
        self.act_game += 1
        A_B_K = self.f.readline().split()
        A = int(A_B_K[0])
        B = int(A_B_K[1])
        K = int(A_B_K[2])
        return A, B, K

    def write_file(self):
        self.output = open(self.filename+'.out', 'w')

    def write_single_game(self, nr, chances):
        case_str = '''Case #{}: {}\n'''.format(nr, chances)
        self.output.write(case_str)

    def close_files(self):
        if self.f:
            self.f.close()
        if self.output:
            self.output.close()

class NewLottery():
    def __init__(self, a, b, k):
        self.a = a
        self.b = b
        self.k = k

    def num_to_bin(self, i):
        return None

    def find_chances(self):
        chances = 0
        for i in range(0, self.a):
            for j in range(0, self.b):
                t = i & j
                if  t < self.k:
                    chances += 1
        return chances

if __name__ == '__main__':
    fh = Filehandler('B-small-attempt0.bin')
    fh.read_file()
    fh.write_file()
    for i in range(0, fh.tot_games):
        A, B, K = fh.read_single_game()
        nl = NewLottery(A, B, K)
        chances = nl.find_chances()
        print chances
        fh.write_single_game(i+1, chances)
    fh.close_files()