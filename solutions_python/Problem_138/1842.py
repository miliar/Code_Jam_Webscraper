__author__ = 'thomas'

#[]
#{}
#\


class WarGame(object):
    def __init__(self, weights_naomi=[], weights_ken= []):
        self.weights_naomi = weights_naomi
        self.weights_ken = weights_ken
        self.score_naomi = 0
        self.score_ken = 0

    def decide_blocks(self, block_naomi, block_ken):
        if block_naomi > block_ken:
            self.score_naomi += 1
        else:
            self.score_ken += 1

    def ken_chooses(self, weight_naomi):
        weight_ken = min(self.weights_ken)
        for weight in self.weights_ken:
            if weight > weight_naomi:
                if weight_ken > weight_naomi:
                    if weight < weight_ken:
                        weight_ken = weight
                else:
                    weight_ken = weight
        return weight_ken


class DeceitefulWar(WarGame):
    def __init__(self, weights_naomi=[], weights_ken=[]):
        super(DeceitefulWar, self).__init__(weights_naomi, weights_ken)

    def play_game(self):
        self.weights_naomi.sort()
        self.weights_ken.sort()
        while len(self.weights_naomi) > 0:
            weight_naomi = self.weights_naomi[0]
            self.weights_naomi.remove(weight_naomi)
            if weight_naomi < self.weights_ken[0]:
                tell_naomi = self.weights_ken[-1] - 0.00000001
            else:
                tell_naomi = self.weights_ken[-1] + 0.00000001
            weight_ken = self.ken_chooses(tell_naomi)
            self.weights_ken.remove(weight_ken)
            self.decide_blocks(weight_naomi, weight_ken)
        return self.score_naomi, self.score_ken


class War(WarGame):
    def __init__(self, weights_naomi=[], weights_ken=[]):
        super(War, self).__init__(weights_naomi, weights_ken)

    def play_game(self):
        while len(self.weights_naomi) > 0:
            weight_naomi = self.weights_naomi[0]
            self.weights_naomi.remove(weight_naomi)
            weight_ken = self.ken_chooses(weight_naomi)
            self.weights_ken.remove(weight_ken)
            self.decide_blocks(weight_naomi, weight_ken)
        return self.score_naomi, self.score_ken


class Filehandler():
    def __init__(self, filename=None):
        self.filename = filename
        self.tot_games = None
        self.act_game = 0
        self.num_weights = 0
        self.f = None
        self.output = None
        _filename = filename + '.out'

    def read_file(self):
        self.f = open(self.filename, 'r')
        self.tot_games = int(self.f.readline())

    def read_single_game(self):
        self.act_game += 1
        self.num_weights = int(self.f.readline())
        weights_1 = self.f.readline().split()
        weights_2 = self.f.readline().split()
        return [float(i) for i in weights_1], [float(i) for i in weights_2]

    def write_file(self):
        self.output = open(self.filename+'.out', 'w')

    def write_single_game(self, nr, score_naomi_dw, score_naomi_w):
        case_str = '''Case #{}: {} {}\n'''.format(nr, score_naomi_dw, score_naomi_w)
        self.output.write(case_str)

    def close_files(self):
        if self.f:
            self.f.close()
        if self.output:
            self.output.close()

if __name__ == '__main__':

    fh = Filehandler('D-large.bin')
    fh.read_file()
    fh.write_file()
    for i in range(0, fh.tot_games):
        w1, w2 = fh.read_single_game()
        w = War(list(w1), list(w2))
        dw = DeceitefulWar(list(w1), list(w2))
        score_naomi_war, _ = w.play_game()
        score_naomi_dwar, _ = dw.play_game()
        fh.write_single_game(i+1, score_naomi_dwar, score_naomi_war)
    fh.close_files()