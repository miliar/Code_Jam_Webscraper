'''
Created on 13.04.2013

@author: Great Combinator
'''
import math

class FairSquare(object):
    def __init__(self, inp, outp, arity, max):
        self.input_path = inp
        self.output_path = outp
        self.numberOfTCs = 0
        self.max_arity = arity
        self.max_number = max
        self.fair_squares = self.compute_fair_squares(1, self.max_number)
        
    def compute_fair_squares(self, min, max):
        fair_squares = {}
        fairs = self.get_fair_numbers(1, int(math.floor(math.sqrt(float(max)))))
        for fair in fairs:
            square = math.pow(fair, 2)
            if self.is_fair(square):
                fair_squares[fair] = square
        return fair_squares
    
    def is_fair(self, number):
        is_fair = True
        string_repr = repr(int(number))
        front_idx = 0
        back_idx = len(string_repr)-1
        if not string_repr[back_idx].isdigit():
            back_idx -= 1
        while front_idx <= back_idx:
            #print string_repr[front_idx], string_repr[back_idx]
            if string_repr[front_idx] != string_repr[back_idx]:
                is_fair = False
                break
            front_idx += 1
            back_idx -= 1
        #print 'CHECK', string_repr, is_fair
        return is_fair
    
    def count_fair_square(self, A, B):
        lower_border = math.ceil(math.sqrt(float(A)))
        upper_border = math.floor(math.sqrt(float(B)))
        counter = 0
        keys = self.fair_squares.keys()
        keys.sort()
        lower_idx = 0
        while lower_idx < len(keys) and keys[lower_idx] < lower_border:
            lower_idx += 1
        upper_idx = len(keys)-1
        while upper_idx < len(keys) and keys[upper_idx] > upper_border:
            upper_idx -= 1
        counter = upper_idx - lower_idx + 1
        if counter < 0:
            counter = 0
        return counter
    
    def is_even(self, number):
        return number%2==0
    
    def get_digits(self, number):
        return int(math.floor(math.log10(number)+1))
    
    def get_fair_numbers(self, minimum_number, maximum_number):
        
        max_digits = self.get_digits(maximum_number)
        n = self.get_digits(minimum_number)
        fair_numbers = []
        while n <= max_digits:
            part = int(math.ceil(float(n)/2.0))
            floor = 1
            ceil = 9
            idx = 1
            while idx < part:
                floor *= 10
                idx += 1
            idx = 1
            while idx < part:
                ceil = ceil*10+9
                idx+=1
            #print 'Check', floor, ceil, part
            idx = floor
            while idx <= ceil:
                s = list('%d'%idx)
                reversed_s = list(s)
                reversed_s.reverse()
                fair_number = None
                if self.is_even(n):
                    fair_number = ''.join(s+reversed_s)
                else:
                    fair_number = ''.join(s+reversed_s[1:])
                idx += 1
                fair_number = int(fair_number)
                if fair_number > maximum_number:
                    return fair_numbers
                elif fair_number >= minimum_number:
                    fair_numbers.append(fair_number)
                    #print fair_number
            n += 1
        
            
    def solve(self):
        input_file = open(self.input_path, 'r')
        output_file = open(self.output_path, 'w')
        idx = 0
        for line in input_file:
            if idx == 0:
                self.numberOfTCs = int(line.strip())
            else:
                interval = line.strip().split(' ')
                A = interval[0]
                B = interval[1]
                output_file.write('Case #%s: %s\n' % (idx, self.count_fair_square(A, B)))
                
            idx += 1
            
        input_file.close()
        output_file.close()            
            
def main():
    input_path = r'C:\Users\Great Combinator\workspace\GCJ2013\fair_and_square\C-large-1.in'
    output_path = r'C:\Users\Great Combinator\workspace\GCJ2013\fair_and_square\C-large-1.out'
    problem = FairSquare(input_path, output_path, 3, math.pow(10, 14))
    problem.solve()
    #print problem.get_fair_numbers(1, 4)
    #print problem.compute_fair_squares(1, math.pow(10, 14))
    
if __name__ == '__main__':
    main()