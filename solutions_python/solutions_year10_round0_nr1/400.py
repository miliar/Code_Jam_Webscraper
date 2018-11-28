#!/usr/bin/python

import sys

def is_light_on(N, K):
    """Given N and K return 'ON' or 'OFF'"""
    p2 = K+1
    # The state is ON only if the next state multiplo of 2^N
    base = 2**N
    if p2 % base == 0:
        return "ON"
    else:
        return "OFF"

def main(nameIn, nameOut):
    """Read form the input and write thr Case #:"""

    
    fI = open(nameIn, 'r')
    fO = open(nameOut, 'w')

    # First line is the number of cases
    l = fI.readline()
    Nl = int(l[0:-1])

    i=0    
    for line in fI:
        line = line.strip() # This will remove the \n also
        if len(line)==0:
            continue
        i += 1
        if i>Nl:
            break
        (N,K) = [ int(x) for x in line.split() ]
        fO.write("Case #" + str(i) + ": " + is_light_on(N,K) + "\n")
    fI.close()
    fO.close()


if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: " + sys.argv[0] + " <file_in> <file_out>")
        exit(0)

    main(sys.argv[1], sys.argv[2])

    
