#from _commons.data import init_logging
import codecs
import logging

PROJECT_NAME = 'codejam2015c'
INPUT_FILE = '../data/' + PROJECT_NAME + '/input.in'
OUTPUT_FILE = '../data/' + PROJECT_NAME + '/output.txt'

# Initiate logger
#init_logging(logging.INFO)


class Multiplier():
    
    values = None
    index = None
    
    @classmethod
    def init(cls):

        cls.index = {}
        cls.index['1'] = 0
        cls.index['i'] = 1
        cls.index['j'] = 2
        cls.index['k'] = 3
        
        cls.values = [[0 for x in range(4)] for x in range(4)]
        cls.setMatrixValue('1', '1', '1')
        cls.setMatrixValue('1', 'i', 'i')
        cls.setMatrixValue('1', 'j', 'j')
        cls.setMatrixValue('1', 'k', 'k')
        cls.setMatrixValue('i', '1', '1')
        cls.setMatrixValue('i', 'i', '-1')
        cls.setMatrixValue('i', 'j', 'k')
        cls.setMatrixValue('i', 'k', '-j')
        cls.setMatrixValue('j', '1', 'j')
        cls.setMatrixValue('j', 'i', '-k')
        cls.setMatrixValue('j', 'j', '-1')
        cls.setMatrixValue('j', 'k', 'i')
        cls.setMatrixValue('k', '1', 'k')
        cls.setMatrixValue('k', 'i', 'j')
        cls.setMatrixValue('k', 'j', '-i')
        cls.setMatrixValue('k', 'k', '-1')
    
    @classmethod
    def setMatrixValue(cls, a, b, result):
            cls.values[cls.index[a]][cls.index[b]] = result
    
    @classmethod
    def getMatrixValue(cls, a, b):
            return cls.values[cls.index[a]][cls.index[b]]
            
    @classmethod
    def multiply(cls, a, b):
        if not cls.values:
            cls.init()
        
        a_sign = b_sign = res_sign = ''
        if '-' in a:
            a_sign = '-'
            a = a[1]
        if '-' in b:
            b_sign = '-'
            b = b[1]
        
        res = cls.getMatrixValue(a, b)
        if '-' in res:
            res_sign = '-'
            res = res[1]
        
        total_sign = a_sign + b_sign + res_sign
        if '--' in total_sign:
            total_sign = total_sign[:-2]
        
        return total_sign + res



class TestCase():

    multipler = Multiplier()
    number = None
    word = None
    
    def __init__(self, number, word):
        self.number = number
        self.word = word
        logging.debug(self)
    
    def find_i(self):
        found = []
        i = 0
        current_result = self.word[i]
        while i < len(self.word) - 1:
            logging.debug('current_result : %s', current_result)
            if current_result == 'i':
                found.append(i)
            i += 1
            current_result = Multiplier.multiply(current_result, self.word[i])
        return found
            
    def find_j(self, i_positions):
        found = []
        for position in i_positions:
            i = position + 1
            if i >= len(self.word):
                break
            if not self.verify_2_sum(i):
                logging.info('Case #%d - 2-sum verif failed.', self.number)
                break
            current_result = self.word[i]
            while i < len(self.word) - 1:
                logging.debug('current_result : %s', current_result)
                if current_result == 'j':
                    found.append(i)
                i += 1
                current_result = Multiplier.multiply(current_result, self.word[i])
        return found
        
    def find_k(self, j_positions):
        for position in j_positions:
            if position >= len(self.word):
                break
            i = position + 1
            current_result = self.word[i]
            while i < len(self.word) - 1:
                logging.debug('current_result : %s', current_result)
                i += 1
                current_result = Multiplier.multiply(current_result, self.word[i])
                
        return current_result == 'k'
        
    def verify_3_sum(self):
        i = 0
        current_result = self.word[i]
        while i < len(self.word) - 1:
            logging.debug('current_result : %s', current_result)
            i += 1
            current_result = Multiplier.multiply(current_result, self.word[i])
        return current_result == '-1'
    
    def verify_2_sum(self, start):
        i = start
        current_result = self.word[i]
        while i < len(self.word) - 1:
            logging.debug('current_result : %s', current_result)
            i += 1
            current_result = Multiplier.multiply(current_result, self.word[i])
        return current_result == 'i'
    
    def has_matching(self):
        
        if not self.verify_3_sum():
            logging.info('Case #%d - 3-sum verif failed.', self.number)
            return False
        
        found_i = self.find_i()
        logging.info('Case #%d - Found i : %s', self.number, found_i)
        if not found_i:
            return False
        
        found_j = self.find_j(found_i)
        logging.info('Case #%d - Found j : %s', self.number, found_j)
        if not found_j:
            return False
        
        if self.find_k(found_j):
            logging.info('Case #%d - Ends with k !', self.number)            
            return True
        else:
            logging.info('Case #%d - Failed', self.number)   
            return False
    
    def __repr__(self):
        return 'Case#%d : %s' % (self.number, self.word)



class Main():
    
    cases = []
    
    def run(self):
        self.parse_input()

        solutions = []
        for case in self.cases:
            answer = 'YES' if case.has_matching() else 'NO'
            case_line = 'Case #%d: %s' % (case.number, answer)
            solutions.append(case_line)
            
        self.write_output(solutions)
        
    def parse_input(self):
        with codecs.open(INPUT_FILE, 'r', 'utf-8') as input_file:
            input_file.readline()
            i = 0
            while True:
                i += 1
                line1 = input_file.readline()
                if not line1:
                    break
                repetitions = int(line1.strip().split()[1])
                pattern = input_file.readline().strip()
                logging.debug("Pattern : %s", pattern)
                self.cases.append(TestCase(i, pattern * repetitions))           
                
    def write_output(self, lines):
        output_file = codecs.open(OUTPUT_FILE, 'w', 'utf-8')
        for line in lines:
            output_file.write(line + '\n')
        output_file.close()
    
    def __init__(self):
        logging.info('Start')
        self.run()
        logging.info('End')


Main()