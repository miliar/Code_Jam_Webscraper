'''
Created on 14-04-2012

@author: Marta
'''
import string

def read_learning_files(gtextf, englishtextf):
    gfile = open(gtextf, 'r')
    efile = open(englishtextf, 'r')
    translator = {}
    for gletter, eletter in zip(gfile.read(), efile.read()) :
        translator[gletter] = eletter
    gfile.close()
    efile.close()
    translator['q'] = 'z'
    translator['z'] = 'q'
    return translator
    
gtextf = '../input/learn_input'
englishtextf =  '../output/learn_output'


def translate(line, trans):
    translated = ''
    for letter in string.lower(line):
        translated += trans[letter]
    return translated

def translate_test_cases(input_file, output_file):
    trans = read_learning_files(gtextf, englishtextf)
    input = open(input_file, 'r')
    output = open(output_file, 'w+')
    #don't care about lines count
    input.readline()
    i = 0
    for line in input.readlines():
        i += 1
        starting = 'Case #%d: ' %i
        translated = translate(line, trans)
        output.write(starting + translated)
    
translate_test_cases('../input/A-small-attempt0.in', '../output/output_0')