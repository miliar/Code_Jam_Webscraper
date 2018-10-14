__author__ = 'PavelM'


class MagicTrick:

    def __init__(self, input):
        self.guess1 = int(input.readline())
        board1 = []
        for k in range(4):
            s = input.readline()
            a = map(int, s.split())
            board1.append(a)
        self.board1 = board1
        self.guess2 = int(input.readline())
        board2 = []
        for k in range(4):
            s = input.readline()
            a = map(int, s.split())
            board2.append(a)
        self.board2 = board2


    def __call__(self, *args, **kwargs):
        s1 = set(self.board1[self.guess1 - 1])
        s2 = set(self.board2[self.guess2 - 1])
        s = s1.intersection(s2)
        n = len(s)
        if n == 1:
            return s.pop()
        elif n > 1:
            return "Bad magician!"
        else:
            return "Volunteer cheated!"







if __name__ == '__main__':
    with open('A-small-attempt0.out', 'w') as output:
        with open('A-small-attempt0.in') as input:
            n = int(input.readline())
            for k in range(1, n+1):
                trick = MagicTrick(input)
                output.write('Case #{0}: {1}\n'.format(k, trick()))