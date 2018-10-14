import math, re, sys

class InputError(Exception):
    pass


class Input(object):
    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.__line_words = []
        self.__next_word = None
        self.__num_words = 0
    def _get_line(self):
        return self.input_stream.readline().strip()
    def get_line(self):
        self.__line_words = self._get_line().split()
        self.__num_words = len(self.__line_words)
        self.__next_word = 0

    def read_word(self):
        if self.__next_word == None:
            raise InputError("No words left on the current line")
        word = self.__line_words[self.__next_word]
        self.__next_word += 1
        if self.__next_word >= self.__num_words:
            self.__next_word = None
        return word

    def read_line_list(self, ltype):
        if self.__next_word == None:
            self.get_line()
        result = []
        while True:
            try:
                result.append(ltype(self.read_word()))
            except InputError:
                break
        return result

    def read_line(self, *args):
        if self.__next_word == None:
            self.get_line()
        a = 0
        result = []
        while True:
            try:
                result.append(args[a](self.read_word()))
                if a + 1 < len(args): a += 1
            except InputError:
                break
        if len(result) == 1:
            return result[0]
        return result

    def read_line_into_container(self, container, atype):
        while True:
            try:
                container.append(atype(self.read_word()))
            except InputError:
                break



class TestCase(object):
    def __init__(self, input):
        self.N, self.K = input.read_line(int, int)
        self.rows=self.N
        self.cols=self.N
        self.board = []
        for n in range(self.N):
            self.board.append([c for c in input.read_line(str)])
        for row in range(self.N):
            self.fall_row(row)
        self.shrink()
        self.find_wins()
        if self.win['R'] and self.win['B']:
            self.result ='Both'
        elif self.win['R']:
            self.result = 'Red'
        elif self.win['B']:
            self.result = 'Blue'
        else:
            self.result ='Neither'
    def print_board(self):
        for i in range(self.rows):
            print ''.join(self.board[i])
    def fall_row(self, row):
        p = self.N-1
        new_row =[]
        r = self.board[row]
        r.reverse()
        for c in r:
            if c == 'R' or c == 'B':
                new_row.append(c)
        new_row = new_row+['.']*(self.N-len(new_row))
        new_row.reverse()
        self.board[row]=new_row

    def shrink(self):
        self.min_r, self.min_c = self.N, self.N
        self.max_r, self.max_c = -1, -1
        for r in range(self.N):
            for c in range(self.N):
                if self.board[r][c]!='.':
                    self.min_r = min(self.min_r, r)
                    self.max_r = max(self.max_r, r)
                    self.min_c = min(self.min_c, c)
                    self.max_c = max(self.max_c, c)
        new_board = []
        for r in range(self.min_r, self.max_r+1):
            new_board.append(''.join([self.board[r][c] for c in range(self.min_c, self.max_c+1)]))
        self.board= new_board
        self.rows = len(new_board)
        if self.rows==0:
            self.cols=0
        else:
            self.cols = len(new_board[0])


    def find_wins(self):
        self.win = {'R':False, 'B':False}
        if self.rows <self.K and self.cols < self.K:
            return
        rwin_re = re.compile('R'*self.K)
        bwin_re = re.compile('B'*self.K)
        board_string = self.as_rows()+'\n\n'+self.as_cols()+'\n\n'+self.as_se()+'\n\n'+self.as_sw()

        if rwin_re.search(board_string):
            self.win['R']=True
        if bwin_re.search(board_string):
            self.win['B']=True


    def as_rows(self):
        return '\n'.join([''.join(self.board[r]) for r in range(self.rows)])

    def as_cols(self):
        return '\n'.join([''.join([self.board[r][c] for r in range(self.rows)]) for c in range(self.cols)])

    def as_se(self):
        result = []
        C = min(self.rows, self.cols)
        for j in range(2*C):
            row = []
            for i in range(0, min(j, self.cols)+1):
                try:
                    row.append(self.board[j-i][i])
                except IndexError:
                    pass
            result.append(''.join(row))
        return '\n'.join(result)

    def as_sw(self):
        result = []
        C = min(self.rows, self.cols)
        for j in range(2*C):
            row = []
            for i in range(0, min(j, self.cols)+1):
                if j-i>=0 and self.cols-1-i>=0:
                    try:
                        row.append(self.board[j-i][self.cols-1-i])
                    except IndexError:
                        pass
            result.append(''.join(row))
        return '\n'.join(result)



def main():
    input = Input(sys.stdin)
    N = input.read_line(int)
    for n in range(1, N+1):
        sys.stderr.write("case #%d/%d\n"%(n,N))
        case = TestCase(input)
        sys.stdout.write("Case #%d: %s\n"%(n, case.result))

main()








