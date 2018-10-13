# -*- coding: utf-8 -*-
'''
Created on 8 avr. 2017

@author: Marc Césarine
'''

import sys
import os
import argparse
#import re


def Process(content):
    results = []

    content = parseContent(content)
    print(content)
    for i in range(0, len(content)):
        #print('Case #', i)
        exercice = int(content[i])
        exercice_str = str(exercice)
        exercice_array = [int(car) for car in str(exercice)]
        # TODO
        result = []
        if exercice < 10:
            result = exercice_array
        else:
            #print(exercice)
            #print(range(len(exercice_array) - 1, 0, -1))
            for counter in range(len(exercice_array) - 1, -1, -1):
                #print(counter)
                if counter != 0:
                    current_digit = exercice_array[counter]
                    previous_digit = exercice_array[counter - 1]
                    if current_digit < previous_digit:
                        current_digit = 9
                        previous_digit = previous_digit - 1
                        exercice_array[counter - 1] = previous_digit
                        result = [9 for i in range(0, len(result))]
                    result.append(current_digit)
                else:
                    if exercice_array[counter] != 0:
                        result.append(exercice_array[counter])
                #result += digit

        results.append(''.join(map(str, result[::-1])))
    return results


def parseContent(content):
    result = []

    excercices_nb = int(content[0])
    #print(content)
    for i in range(1, excercices_nb + 1):
        exercice = {}

        # TODO

        result.append(content[i])

    return result


def main(argv=None):
    if argv is None:
        argv = sys.argv

    #arguments parser
    parser = argparse.ArgumentParser(description='Launch GoogleCodeJam program')
    parser.add_argument('--input',
                        '-i',
                        nargs=1,
                        help='the input file to process',
                        required=True)

    args = parser.parse_args()

    #creating files path
    currentFolder = os.path.dirname(os.path.realpath(__file__))
    inputFile = os.path.join(currentFolder, args.input[0])

    #Importing input file content
    input_ = open(inputFile, "r")
    content = input_.read()
    contentArray = content.splitlines()
    input_.close()

    #Treating content
    outputArray = Process(contentArray)

    #Writing output file
    outputFile = currentFolder + '/' + '.'.join(args.input[0].split('.')[:-1]) + '.out'
    output = open(outputFile, 'w')
    counter = 1
    for line in outputArray:
        output.write('Case #{0}: {1}\n'.format(str(counter), line))
        print('Case #{0}: {1}\n'.format(str(counter), line))
        counter += 1
    output.close()

if __name__ == "__main__":
    sys.exit(main())
