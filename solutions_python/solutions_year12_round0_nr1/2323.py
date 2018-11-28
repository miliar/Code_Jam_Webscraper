#!/usr/bin/env python
'''
Created on Apr 14, 2012

@author: san
'''
import sys


def main():
        mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 
                   'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p',
                   'w':'f', 'x':'m', 'y':'a', 'z':'q', '\n':'\n', ' ':' '}
        input_file = open(sys.argv[1])
        output_file = open(sys.argv[2], 'w')
        no_cases = int(input_file.readline())
        for i in range(no_cases):
            output_file.write('Case #' + str(i + 1) + ': ')
            line = input_file.readline()
            for char in line:
                output_file.write(mapping[char])
        input_file.close()
        output_file.close()
        

if __name__ == '__main__':
    main()
