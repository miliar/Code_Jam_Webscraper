#! /usr/bin/env python
import numpy as np
import sys

def read_input():
    with open(sys.argv[1]) as in_file:
        num_cases = int(in_file.readline())
        for i in xrange(num_cases):
            lawn = np.empty([int(token) for token in in_file.readline().split()])
            for j in xrange(lawn.shape[0]):
                lawn[j] = np.array([int(token) for token in in_file.readline().split()])
            yield lawn

def valid_lawn(lawn):
    if lawn.min() < 1 or lawn.max() > 100:
        return False
    old_lawn = np.empty([0, 0])
    while old_lawn.shape != lawn.shape:
        old_lawn = lawn
        lawn_min = lawn.min()
        lawn_max = lawn.max()
        if lawn_min == lawn_max:
            return True
        else:
            lawn -= lawn_min
            lawn = lawn[lawn.any(1)]
            lawn = lawn[:, lawn.any(0)]
    return False
            
            

def main():
    with open(sys.argv[2], 'w') as out_file:
        for i, lawn in enumerate(read_input(), start=1):
            out_string = 'Case #{}: '.format(i)
            if valid_lawn(lawn):
                out_string += 'YES\n'
            else:
                out_string += 'NO\n'
            out_file.write(out_string)

if __name__ == '__main__':
    # run as $ python lawnmower.py input.txt output.txt
    main()
