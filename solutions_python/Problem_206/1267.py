#!/bin/env python3

import sys
import os
from decimal import *


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
    myiter = iter(range(len(list(filter(None, lines)))))
    case = 1
    for i in myiter:
        destination, competitors = map(int, lines[i].split())
        
        worst_horse_time = 0 # worst horse will reach dest in x hours
        for competitor in range(competitors):
            next(myiter, None)
            i += 1
            distance, speed = map(int, lines[i].split())

            if (destination-distance)/speed > worst_horse_time:
                worst_horse_time = (destination-distance)/speed
 
        print('Case #' + str(case) + ': ' + str((Decimal(destination) / Decimal(worst_horse_time)).quantize(Decimal('.000001'), rounding=ROUND_HALF_UP)))
        case += 1



if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        print("Usage : " + sys.argv[0] + " filename")
    else:
        doChallenge(sys.argv[1])
