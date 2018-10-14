#!/usr/bin/env python

import os, sys
import codejam

set50 = ( 0,  2,  4,  5,  6,  8,
         10, 12, 14, 15, 16, 18,
         20, 22, 24, 25, 26, 28,
         30, 32, 34, 35, 36, 38,
         40, 42, 44, 45, 46, 48,
         50, 52, 54, 55, 56, 58,
         60, 62, 64, 65, 66, 68,
         70, 72, 74, 75, 76, 78,
         80, 82, 84, 85, 86, 88,
         90, 92, 94, 95, 96, 98,
         100)

set25 = ( 0,      4,  5,      8,
         10, 12,     15, 16,
         20,     24, 25,     28,
         30, 32,     35, 36,
         40,     44, 45,     48,
         50, 52,     55, 56,
         60,     64, 65,     68,
         70, 72,     75, 76,
         80,     84, 85,     88,
         90, 92,     95, 96,
         100)

set20 = ( 0,  5,
         10, 15,
         20, 25,
         30, 35,
         40, 45,
         50, 55,
         60, 65,
         70, 75,
         80, 85,
         90, 95,
         100)

set10 = ( 0,
         10,
         20, 25,
         30, 
         40, 
         50, 
         60, 
         70, 75,
         80, 
         90, 
         100)

set5 = ( 0,
         20, 25,
         40, 
         50, 
         60, 
         75, 80,
         100)

set4 = ( 0,
         25,
         50, 
         75,
         100)

set2 = ( 0,
         50, 
         100)

set1 = ( 0,
         100)


def freecell(testcase):
    if len(testcase) != 1:
        raise RuntimeError, "Oops, we got a bad testcase!"
    vals = [int(x) for x in testcase[0].split(" ")]
    if len(vals) != 3:
        raise RuntimeError, "Oops, we got %d values when we were told 3" % len(vals)
    n = vals[0]
    pd = vals[1]
    pg = vals[2]
    # Check for nonsensical values.
    if pg > 100 or pg < 0 or pd > 100 or pd < 0:
        return "Broken"
    # Check for all correct but not today
    if pg == 100 and pd != 100:
        return "Broken"
    # Check for all wrong but not today
    if pg == 0 and pd != 0:
        return "Broken"
    # For more than 100 games we assume we only played 100 (which means we're ok)
    if n >= 100:
        return "Possible"
    elif n >= 50 and pd in set50:
        return "Possible"
    elif n >= 25 and pd in set25:
        return "Possible"
    elif n >= 20 and pd in set20:
        return "Possible"
    elif n >= 10 and pd in set10:
        return "Possible"
    elif n >= 5 and pd in set5:
        return "Possible"
    elif n >= 4 and pd in set4:
        return "Possible"
    elif n >= 2 and pd in set2:
        return "Possible"
    elif n >= 1 and pd in set1:
        return "Possible"
    return "Broken"

if __name__ == "__main__":
    codejam.main(sys.argv[1:], freecell, 1)
