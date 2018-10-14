#!/bin/env python3

import sys
import os
import re


def doChallenge(_input_filename):
    try:
        with open(_input_filename, 'r') as f:
            lines = f.read().split('\n')
    except FileNotFoundError:
        print("Input file '" + _input_filename + "' not found !")
        sys.exit()
    except PermissionError:
        print("Input file '" + _input_filename + "' could not be read !")
        sys.exit()
    except Exception:
        print("Unknown shit has happened")
        sys.exit()

    del lines[0] # First line is useless
    for i in range(len(list(filter(None, lines)))):
        row, size = lines[i].split()
        res = 0
        ##first step, count then replace all '-' of correct size 
        #res = len(re.findall('-'*int(size), row))
        #row = re.sub('-'*int(size), '+'*int(size), row)

        ##second step, remove all '+' of the correct size (optimization)
        #row = re.sub('\+'*int(size), '', row)

        #check if already won
        if len(re.findall('-', row)) == 0:
            print('Case #' + str(i+1) + ': ' + str(res))
            continue

        #then, replace from left to right
        toggle = {'-':'+', '+':'-'}
        for j in range(len(row)):
            if row[j] == '+':
                continue
            else:
                if len(row[j:j+int(size)]) < int(size): #if we are at the end of the row
                    break
                else:
                    res += 1
                    _ = row[0:j]
                    for z in row[j:j+int(size)]:
                        _ += toggle[z]
                    row = _ + row[j+int(size):]

        #check result
        if len(re.findall('-', row)) == 0:
            print('Case #' + str(i+1) + ': ' + str(res))
        else:
            print('Case #' + str(i+1) + ': IMPOSSIBLE')


if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        print("Usage : " + sys.argv[0] + " filename")
    else:
        doChallenge(sys.argv[1])
