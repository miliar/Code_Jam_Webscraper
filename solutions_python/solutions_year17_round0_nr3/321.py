import sys, logging, random, math
import numpy as np
from collections import defaultdict

# ------- SETUP APPLICATION -----
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
sys.setrecursionlimit(1000)
NOINPUT = False
# ---- INPUT / OUTPUT SETUP -----
# Create an output filename from the standard competition input dataset names
def outputFilenameFromInput(infilename):
    # STD filename of input [char]-[small/large]-practice.in.txt
    name = infilename.split('.')[0]
    if len(name.split('-')) >= 2:
        return name.split('-')[1] + ".txt"
    else:
        return name + ".txt"

if not NOINPUT:
    if len(sys.argv) != 2:
        print("ERROR. Correct usage: python scipt.py file")
        sys.exit(0)
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

def solve(N, K):
    field = [N]
    for i in range(0,K-1):
        logging.debug("Field before %s",field)
        # Get max counter
        maxvalue = max(field)
        maxindex = field.index(maxvalue)
        maxdiv = (maxvalue-1) / 2
        logging.debug("Splitting %d", maxvalue)
        # Divide
        pivot = []
        if math.floor(maxdiv) > 0:
            pivot.append(math.floor(maxdiv))
        if math.ceil(maxdiv) > 0:
            pivot.append(math.ceil(maxdiv))
        field = field[:maxindex] + pivot + field[maxindex+1:]
        logging.debug("Field after %s",field)
    # Getting results
    maxdist = math.ceil((max(field)-1)/2)
    mindist = math.floor((max(field)-1)/2)
    return (maxdist,mindist)

def split(field, threshold):
    maxvalue = max(field.keys())
    times = field[maxvalue]
    if maxvalue <= 1:
        return times+1
    maxdiv = (maxvalue-1) // 2
    maxcar = (maxvalue-1) % 2
    # Divide
    if times < threshold:
        if maxdiv > 0:
            field[maxdiv] += times
            field[maxdiv+maxcar] += times
        # Remove
        field.pop(maxvalue, None)
        return times
    else:
        if maxdiv > 0:
            field[maxdiv] += threshold
            field[maxdiv+maxcar] += threshold
        field[maxvalue] -= threshold
        return threshold

def single_split(field):
    maxvalue = max(field.keys())
    times = field[maxvalue]
    if maxvalue <= 1:
        return times+1
    maxdiv = (maxvalue-1) // 2
    maxcar = (maxvalue-1) % 2
    # Divide
    if maxdiv > 0:
        field[maxdiv] += 1
    field[maxdiv+maxcar] += 1
    # Remove
    if field[maxvalue] <= 1:
        field.pop(maxvalue, None)
    else:
        field[maxvalue]-=1
    return 1

def solveDict(N, K):
    if N==K:
        return (0,0)
    field = defaultdict(int)
    field[N] = 1
    while K > 1:
        logging.debug("Solving K=%d",K)
        K -= split(field, K)
        logging.debug("Field after %s",field)
    # Getting results
    maxvalue = max(field.keys())
    maxdiv = (maxvalue-1) // 2
    maxcar = (maxvalue-1) % 2
    return (maxdiv+maxcar,maxdiv)

if not NOINPUT:
    # Read number of test cases
    N = int(input_rows[0])
    input_rows = input_rows[1:]
    # Loop through all the tests
    for i in range(0, N):
        logging.info("Computing case %d", i+1)
        # Compute
        line = [int(x) for x in input_rows[i].split(' ')]
        x = solveDict(line[0],line[1])
        logging.info("Case #%d: %s", i+1, x)
        # Write to output file
        output_file.write("Case #" + str(i+1) + ": " + str(x[0]) + " " + str(x[1]) + "\n")
    # ---------- OUTPUT CLOSE ----------
    output_file.close()
