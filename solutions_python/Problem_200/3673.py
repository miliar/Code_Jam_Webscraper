#!/bin/env python3

import sys
import os


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
        while int(lines[i]) >= 0:
            if sorted(lines[i]) == list(lines[i]):
                print('Case #' + str(int(i+1)) + ': ' + lines[i])
                break
            else:
                for j in range(len(lines[i])-1):
                    if int(lines[i][j]) < int(lines[i][j+1]):
                        continue
                    else:
                        lines[i] = lines[i][:j+1] + '0' * (len(lines[i]) - j - 1)
                        break

                lines[i] = str(int(lines[i]) - 1)



if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        print("Usage : " + sys.argv[0] + " filename")
    else:
        doChallenge(sys.argv[1])
