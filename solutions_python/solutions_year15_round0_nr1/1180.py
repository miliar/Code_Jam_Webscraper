import math
import time
import sys

if __name__ == '__main__':
    
    # Start timer
    start = time.time()

    if len(sys.argv) != 3:
        print 'Usage: python problemA.py <input_file> <output_file>'
        sys.exit(0)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    lines = [line.strip() for line in open(input_file)]
    total = lines.pop(0)

    results = []

    for l in lines:
        # Initialize for the up audience and additional audience necessary
        # Interpret the info
        info = l.split()
        max = int(info[0])
        seq = info[1]
        up = int(seq[0])
        add = 0
        for idx in range(1, max+1):
            current = int(seq[idx])
            if current == 0:
                continue
            elif up >= idx:
                up += current
            else:
                diff = idx - up
                add += diff
                up += diff + current
        results.append(add)

    # output
    f = open(output_file, 'w')
    for i in range(len(results)):
        f.write('Case #' + str(i+1) + ': ' + str(results[i])+'\n')
    f.close()

    # Stop timer
    end = time.time()
    print "Total time use:", end-start, "s"