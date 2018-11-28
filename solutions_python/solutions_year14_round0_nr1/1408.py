# -*- coding: utf-8 -*-
'''
Created on 11 avr. 2014

@author: Marc Césarine
'''

import sys
import os
import argparse
#import re


def Process(content):
    result = []

    content = parseContent(content)

    for i in range(0, len(content)):
        trick = content[i]
        first_row = trick['first_table'][trick['first_row'] - 1]
        second_row = trick['second_table'][trick['second_row'] - 1]
        common_cards = []
        print('test ' + first_row + ' with ' + second_row)
        for j in str.split(first_row, ' '):
            if j in str.split(second_row, ' '):
                common_cards.append(j)
        print("trick #" + str(i) + " - Nb cards : " + str(len(common_cards)))
        if len(common_cards) == 0:
            result.append('Volunteer cheated!')
        elif len(common_cards) == 1:
            result.append(common_cards[0])
        else:
            result.append('Bad magician!')

    return result


def parseContent(content):
    result = []

    excercices_nb = int(content[0])
    print(content)
    for i in range(0, excercices_nb):
        magician_trick = {}
        counter = 0
        min_index = 1 + (i) * 10
        max_index = min_index + 10
        for j in range(min_index, max_index):
            if counter == 0:
                magician_trick['first_row'] = int(content[j])
                magician_trick['first_table'] = []
            elif counter == 5:
                magician_trick['second_row'] = int(content[j])
                magician_trick['second_table'] = []
            elif counter < 5:
                magician_trick['first_table'].append(content[j])
            elif counter < 10:
                magician_trick['second_table'].append(content[j])
                if counter == 9:
                    result.append(magician_trick)
            counter += 1
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
        counter += 1
    output.close()

if __name__ == "__main__":
    sys.exit(main())
