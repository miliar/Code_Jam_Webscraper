INFILE = r'C:\Users\noam\workspace\CodeJam\input.txt'

class Magicka(object):
    def __init__(self, combine_rules, opposed_rules, letter_sequence):
        self.combine_rules = {}
        self.opposed_rules = {}
        self.letter_sequence = letter_sequence
        self.cur_sequence = ''
        
        #combine rules
        for rule in combine_rules:
            self.combine_rules[(rule[0], rule[1])] = rule[2]
            self.combine_rules[(rule[1], rule[0])] = rule[2]
        
        #opposite rules 
        for rule in opposed_rules:
            self._init_opposed_pair(rule[0], rule[1])
            self._init_opposed_pair(rule[1], rule[0])
    
    def _init_opposed_pair(self, opp1, opp2):
        tmp = self.opposed_rules.get(opp1, [])
        tmp.append(opp2)
        self.opposed_rules[opp1] = tmp
        
    def handle_letter(self, letter):
        if not self.cur_sequence:
            self.cur_sequence += letter
            return
        
        #handle combine
        last_two = (self.cur_sequence[-1], letter)
        combine_res = self.combine_rules.get(last_two)
        if combine_res is not None:
            self.cur_sequence = ''.join(self.cur_sequence[:-1]) + combine_res
            return
        
        #handle opposed
        opposed_list = self.opposed_rules.get(letter)
        if opposed_list is not None:
            for opposed in opposed_list:
                if opposed in self.cur_sequence:
                    self.cur_sequence = ''
                    return
        
        self.cur_sequence += letter
    
    def play(self):
        for letter in self.letter_sequence:
            self.handle_letter(letter)
        return self.cur_sequence

def play(combine_rules, oppsed_rules, letter_sequence):
    m = Magicka(combine_rules, oppsed_rules, letter_sequence)
    ret = m.play()
    return list(ret)
        
def parse_line(line):
    line = line.strip()
    splitted = line.split(' ')
    combines_num = int(splitted[0])
    combine_rules = splitted[1:combines_num+1]
    opposed_num = int(splitted[1+combines_num])
    opposed_rules = splitted[2+combines_num:2+combines_num+opposed_num]
    letter_sequence = splitted[-1]
    return combine_rules, opposed_rules, letter_sequence
     
def main():
    infile = file(INFILE)
    outfile = file(INFILE + '.result.txt', 'wt')
    infile.readline()
    for idx, line in enumerate(infile):
        combine_rules, opposed_rules, letter_sequence = parse_line(line)
        res = play(combine_rules, opposed_rules, letter_sequence)
        str_ret = '[' + ', '.join(res) + ']'
        res_line = 'Case #%d: %s\n' % (idx + 1, str_ret)
        print res_line,
        outfile.write(res_line)
    infile.close()
    outfile.close()
    

if __name__ == '__main__':
    main()