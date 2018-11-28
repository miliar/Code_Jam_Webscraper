import sys, logging, random
import numpy as np
from collections import defaultdict

def solve(D, horses):
    if len(horses)==0:
        return float(D)
    times = []
    for horse in horses:
        l = D - horse[0]
        t = l / horse[1]
        times.append(t)
    return D / max(times)

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

# Read number of test cases
N = int(input_rows[0])
input_rows = input_rows[1:]
# Loop through all the tests
k = 0
for i in range(0, N):
    logging.info("Computing case %d", i+1)
    # Compute
    line0 = input_rows[k].split(' ')
    d = int(line0[0])
    n = int(line0[1])
    k += 1
    horses = []
    for j in range(n):
        lineh = input_rows[k].split(' ')
        horse = (int(lineh[0]), int(lineh[1]))
        horses.append(horse)
        k += 1
    x = solve(d, horses)
    # Write to output file
    output_file.write("Case #" + str(i+1) + ": " + str(x) + "\n")

# ---------- OUTPUT CLOSE ----------
output_file.close()
