import sys
class board (object):
#    def parse_board_str(board_str):
#        return board_str.split('\n');
    def __init__(self, board_data):
        self._data = board_data#parse_board_str(board_str)
    def check_row_winner(self):
        for row in self._data:
            cur = None
            for char in row:
                if char == ".":
                    break
                elif char == "T":
                    continue
                elif cur == None:
                    cur = char
                elif not (cur == char):
                    break
            else:
                return cur
        return None
    def check_col_winner(self):
        for i in range(0,4):
            cur = None
            for char in [row[i] for row in self._data]:
                if char == ".":
                    break
                elif char == "T":
                    continue
                elif cur == None:
                    cur = char
                elif not (cur == char):
                    break
            else:
                return cur
        return None
    def check_diag_winner(self):
        cur = None
        for char in [row[i] for i, row in enumerate(self._data)]:
            if char == ".":
                break
            elif char == "T":
                continue
            elif cur == None:
                cur = char
            elif not (cur == char):
                break
        else:
            return cur
        cur = None
        for char in [row[3-i] for i, row in enumerate(self._data)]:
            if char == ".":
                break
            elif char == "T":
                continue
            elif cur == None:
                cur = char
            elif not (cur == char):
                break
        else:
            return cur
        return None
    def check_finished(self):
        for row in self._data:
            for char in row:
                if char == ".":
                    return False
        return True
    def print_result(self):
        res = self.check_col_winner()
        if not (res == None):
            return res + " won"
        res = self.check_row_winner()
        if not (res == None):
            return res + " won"
        res = self.check_diag_winner()
        if not (res == None):
            return res + " won"
        if (self.check_finished()):
            return "Draw"
        return "Game has not completed"
def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        b = board(split_input[1+(i*5):5+(i*5)])
        output_file.write("Case #" + str(i + 1) + ": " + b.print_result() + "\n")
    
if __name__ == "__main__":
    main()
