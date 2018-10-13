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
    #print(content)
    for i in range(0, len(content)):
        print('Case #',i)
        exercice = content[i]
        exercice['Naomie'].sort()
        exercice['Ken'].sort()

        #print(exercice['Naomie'])
        #print(exercice['Ken'])

        end = False
        i, j, deceitful_result = len(exercice['Naomie']) - 1, len(exercice['Ken']) - 1, 0
        while not end:
            #print(str(exercice['Naomie'][i]),' - ',str(exercice['Ken'][j]))
            if i < 0 or j < 0:
                end = True
            elif exercice['Naomie'][i] > exercice['Ken'][j]:
                i -= 1
                j -= 1
                deceitful_result += 1
            else:
                j -= 1
        #for i in range(0, len(exercice['Naomie'])):
        #print(deceitful_result)

        end = False
        i, j, normal_result = len(exercice['Naomie']) - 1, len(exercice['Ken']) - 1, 0
        while not end:
            if i < 0 or j < 0:
                end = True
            elif exercice['Naomie'][i] < exercice['Ken'][j]:
                i -= 1
                j -= 1
            else:
                #print(str(exercice['Naomie'][i]),' - ',str(exercice['Ken'][j]))
                i -= 1
                normal_result += 1
        #for i in range(0, len(exercice['Naomie'])):
        #print(normal_result)
        result.append(str(deceitful_result) + ' ' + str(normal_result))
    #print(content)
    return result


def parseContent(content):
    result = []

    excercices_nb = int(content[0])
    #print(content)
    for i in range(0, excercices_nb):
        excercice = {}

        naomie_blocks = str.split(content[((i + 1) * 3) - 1], ' ')
        for j in range(0, len(naomie_blocks)):
            naomie_blocks[j] = float(naomie_blocks[j])
        excercice['Naomie'] = naomie_blocks

        ken_blocks = str.split(content[((i + 1) * 3)], ' ')
        for j in range(0, len(ken_blocks)):
            ken_blocks[j] = float(ken_blocks[j])
        excercice['Ken'] = ken_blocks
        result.append(excercice)

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
