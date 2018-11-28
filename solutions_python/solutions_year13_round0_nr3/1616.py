# -*- coding: utf-8 -*-
#Filename: fairandsquare.py

import sys
import math

class FairAndSquare:

    def __init__(self, input_filename, output_filename):
        
        # Generate all fair and square numbers up to 10**100
        print 'Generating fair and square numbers...'
        self.number_list = self.generate_numbers(10**14)
        print 'Done.'
        
        # Open input and output files
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')
        
        # Get the number of cases
        number_of_cases = int(input_file.readline())
        
        # Evaluate all board positions and output the result to the output file
        for case in range(number_of_cases):
            limits = input_file.readline().split()
            result = self.calc_numbers(int(limits[0]), int(limits[1]))
            
            self.output_result(result, case+1, output_file)
    
    # Generates all fair and square numbers up to max
    def generate_numbers(self, max):
        number_list = []
        
        max_reached = False
        cur_root = 1
        while not max_reached:
            if self.is_palindrome(cur_root) and self.is_palindrome(cur_root**2):
                number_list.append(cur_root**2)
                
                if cur_root**2 >= max:
                    max_reached = True
            cur_root += 1
        return number_list
    
    # Determines the number of fair and square numbers within an interval
    def calc_numbers(self, min, max):
        number_of_hits = 0
        for num in self.number_list:
            if num >= min and num <= max:
                number_of_hits += 1
        
        return number_of_hits
    
    # Checks whether an integer is a palindrome
    def is_palindrome(self, number):
        str_num = str(number)
        for i in range(int(math.floor(len(str_num)/2.0))):
            if not (str_num[i] == str_num[-(i+1)]):
                return False
        return True
        
    
    def output_result(self, result, case_nr, output_file):
        output_file.write('Case #{}: {}\n'.format(case_nr, result))

def main(args):
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
    if len(args) == 1:
        input_filename = args[0]
    elif len(args) == 2:
        input_filename = args[0]
        output_filename = args[1]
    else:
        print 'Executing with default input and output filename'
    
    FairAndSquare(input_filename, output_filename)


if __name__ == '__main__':
    main(sys.argv[1:])
