__author__ = 'anoop'

import numpy as np

INPUT_FILE = 'B-small-attempt0.in'
OUTPUT_FILE = 'B-small-attempt0.out'

def main():
    f = open(INPUT_FILE)
    f_out = open(OUTPUT_FILE, "w")
    num_of_trials = int(f.readline()[:-1])
    for sample in range(num_of_trials):
        line = f.readline()[:-1].split(' ')
        line  = map(int, line)
        num1 = line[0]
        num2 = line[1]
        target = line[2]
        count = 0
        for i in range(num1):
            for j in range(num2):

                if (i&j) < target:
                    count = count + 1

        write_sample = sample + 1
        f_out.write("Case #%d: %d\n"%(write_sample, count))

    f.close()
    f_out.close()

if __name__ == "__main__":
    main()