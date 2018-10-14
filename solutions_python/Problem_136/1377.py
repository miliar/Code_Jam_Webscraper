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
    print(content)
    for i in range(0, len(content)):
        excercice = content[i]
        F = excercice['F']
        C = excercice['C']
        X = excercice['X']

        farm_interest = C/F
        print('Case #' + str(i+1))
        #print('interest of a farm : ' + str(farm_interest) + ' seconds')

        end = False
        cookie_production = 2
        cookie_produced = 0
        time_passed = 0
        while not end:
            #print('1')
            if cookie_produced < C:
                if C < X:
                    time_passed += C / cookie_production
                    cookie_produced = C
                else:
                    result.append(round(X / cookie_production, 7))
                    end = True
                #print('time passed : ' + str(time_passed))
            else:
                time_without_farm = (X - cookie_produced) / cookie_production
                time_with_farm = (X - cookie_produced + C) / (cookie_production + F)
                if time_without_farm < time_with_farm:
                    result.append(round(time_passed + time_without_farm, 7))
                    end = True
                else:
                    cookie_production = F + cookie_production
                    time_passed = (C / cookie_production) + time_passed
                    cookie_produced = C
                #print('cookies produced : ' + str(cookie_produced))
                #print('production : ' + str(cookie_production))
                #print('time passed : ' + str(time_passed))

    return result


def parseContent(content):
    result = []

    excercices_nb = int(content[0])
    #print(content)
    for i in range(0, excercices_nb):
        excercice = {}
        splitted_line = str.split(content[i + 1], ' ')
        excercice['C'] = float(splitted_line[0])
        excercice['F'] = float(splitted_line[1])
        excercice['X'] = float(splitted_line[2])
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
