import sys

class Tomek(object):

    def __init__(self, input_fn):
        self.input_filename = input_fn
        self.output_filename = 'results.txt'
        
        self.input = open(self.input_filename, 'r')
        self.output = open(self.output_filename, 'a')

        self.cases = []
        self.cases.append('X won')
        self.cases.append('O won')
        self.cases.append('Draw')
        self.cases.append('Game has not completed')
        
        self.game_id = 1
        self.game_array = []

    def process(self):
        test_cases = int(self.input.readline())
        for i in range(test_cases):
            self.readin_game()
            self.game_array = []

    def readin_game(self):
        for i in range(4):
            self.game_array.append(list(self.input.readline().rstrip()))
        print self.input.readline()
        self.process_gamestate()
        self.game_id += 1
        print self.game_array

    def process_gamestate(self):
        found_output, output_id, pcount = self.check_rows()
        if not found_output:
            print 'not found in rows'
            found_output, output_id = self.check_cols()
            if not found_output: 
                print 'not found in cols'
                found_output, output_id = self.check_forward_diag()
                if not found_output:
                    print 'not found in forward diag'
                    found_output, output_id = self.check_backward_diag()
        if found_output:
            print 'found'
            self.print_output(output_id)
        else:
            print 'not found', str(pcount)
            if pcount > 0:
                self.print_output(3)
            else:
                self.print_output(2)

    def check_rows(self):
        for x in range(4):
            counts = {'X':0, 'O':0, 'T':0, '.':0}
            for y in range(4):
                c = self.game_array[x][y]
                counts[c] += 1
            found, case_id = self.check_counts(counts['X'], counts['O'], counts['T'])
            if found:
                return found, case_id, counts['.']
        return (False, -1, counts['.'])

    def check_counts(self, xcount, ocount, tcount):
            if xcount == 4:
                return (True, 0)
            elif ocount == 4:
                return (True, 1)
            elif xcount == 3 and tcount > 0:
                return (True, 0)
            elif ocount == 3 and tcount > 0:
                return (True, 1)
            return (False, -1)

    def check_cols(self):
        for y in range(4):
            counts = {'X':0, 'O':0, 'T':0, '.':0}
            for x in range(4):
                c = self.game_array[x][y]
                counts[c] += 1
            found, case_id = self.check_counts(counts['X'], counts['O'], counts['T'])
            if found:
                return found, case_id
        return (False, -1)
    
    def check_forward_diag(self):
        counts = {'X':0, 'O':0, 'T':0, '.':0}
        for i in range(4):
            c = self.game_array[i][i]
            counts[c] += 1
            found, case_id = self.check_counts(counts['X'], counts['O'], counts['T'])
            if found:
                return found, case_id
        return (False, -1)

    def check_backward_diag(self):
        counts = {'X':0, 'O':0, 'T':0, '.':0}
        for i in range(4):
            c = self.game_array[3-i][i]
            counts[c] += 1
            found, case_id = self.check_counts(counts['X'], counts['O'], counts['T'])
            if found:
                return found, case_id
        return (False, -1)

    def print_output(self, output_id):
        self.output.write('Case #%s: %s\n' % (self.game_id, self.cases[output_id]))

if __name__ == '__main__':
    INPUT_FILENAME = sys.argv[1]
    tester = Tomek(INPUT_FILENAME)
    tester.process()
