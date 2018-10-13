import sys, logging, random
import numpy as np
from collections import defaultdict

# ------- SETUP APPLICATION -----
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
sys.setrecursionlimit(1000)
# ---- INPUT / OUTPUT SETUP -----
if len(sys.argv) != 2:
    print("ERROR. Correct usage: python scipt.py file")
    sys.exit(0)
# Create an output filename from the standard competition input dataset names
def outputFilenameFromInput(infilename):
    # STD filename of input [char]-[small/large]-practice.in.txt
    name = infilename.split('.')[0]
    if len(name.split('-')) >= 2:
        return name.split('-')[1] + ".txt"
    else:
        return name + ".txt"
#Get the first parameter a.k.a. the input file
FILE_NAME = sys.argv[1]
#Read the file
output_file = open(outputFilenameFromInput(FILE_NAME), 'w')
input_file = open(FILE_NAME, 'r')
input_rows = list(input_file)

# ------- SOLVE BELOW THIS ---------
# Parsing input file to problem vars
# READ SINGLE INT: int(input_rows[i])
# READ INT LIST: [int(x) for x in input_rows[i].split(' ')]
# WRITE LINE: output_file.write(line + "\n")
# ----------------------------------

def decrement(char):
    if (int(char)==0):
        return '9'
    else:
        return str(int(char)-1)

def solve(n):
    # Analyze string by 2 chars, starting from right-most
    # If c(i+1) < c(i) => c(i+i)-1, c(i..0)=9
    # else leave it
    # 1232321
    # 1229999
    res = ""
    while len(n)>1:
        logging.debug("String %s",n)
        logging.debug("Res %s",res)
        if n[-1:] < n[-2:-1]:
            #Put 9s
            res = '9' + '9' * len(res)
            print("N is composed of", n[-2:])
            n = n[:-2] + decrement(n[-2:-1])
        else:
            res = n[-1:] + res
            n = n[:-1]
    # Add the last char
    if n[0] > '0':
        res = n[0] + res
    return res

print(solve('565'))

# Read number of test cases
N = int(input_rows[0])
input_rows = input_rows[1:]
# Loop through all the tests
for i in range(0, N):
    logging.info("Computing case %d", i+1)
    # Compute
    x = solve(input_rows[i][:-1])
    # Write to output file
    output_file.write("Case #" + str(i+1) + ": " + str(x) + "\n")

# ---------- OUTPUT CLOSE ----------
output_file.close()
