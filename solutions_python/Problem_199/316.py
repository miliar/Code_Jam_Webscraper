import sys, logging, random
import numpy as np
from collections import defaultdict

# ------- SETUP APPLICATION -----
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
sys.setrecursionlimit(5000)
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
logging.debug("Loaded %d rows", len(input_rows))

# ------- SOLVE BELOW THIS ---------
# Parsing input file to problem vars
# READ SINGLE INT: int(input_rows[i])
# READ INT LIST: [int(x) for x in input_rows[i].split(' ')]
# WRITE LINE: output_file.write(line + "\n")
# ----------------------------------

def toggle(c):
    if c=='-':
        return '+'
    else:
        return '-'

def swap(s, k, start):
    res = s[:start]
    for i in range(0,k):
        res += toggle(s[i+start])
    res += s[k+start:]
    return res

def solve(s, k, start=0, step=0):
    logging.debug("Anal:", s,k,start,step)
    # Go right till the first -
    fminus = s[start:].find('-') + start
    if s.find('-') == -1:
        return step
    if s[:start].find('-') >= 0:
        return -1
    if fminus > len(s) - k:
        return -1
    #Swap
    return solve(swap(s, k, fminus), k, fminus+1, step+1)

# Read number of test cases
N = int(input_rows[0])
input_rows = input_rows[1:]
# Loop through all the tests
for i in range(0, N):
    logging.info("Computing case %d", i+1)
    line = input_rows[i].split(' ')
    # Compute
    logging.debug("Solving", line[0], line[1])
    x = solve(line[0], int(line[1]))
    if x<0:
        x = "IMPOSSIBLE"
    # Write to output file
    output_file.write("Case #" + str(i+1) + ": " + str(x) + "\n")

# ---------- OUTPUT CLOSE ----------
output_file.close()
