import numpy as np
import sys

def main(input, output):
    f = open(output, 'w')
    num = None
    loop = 1
    for line in file(input):
        if num is None:
            num = int(line.strip())
            continue
        elements = np.array(map(int, line.strip().split(' ')))
        N = elements[0]
        S = elements[1]
        p = elements[2]
        total_googlers = 0
        for i in range(3, 3 + N):
            current_sum = elements[i]

            if current_sum < p:
                continue
            
            surprise = (p * 3) - 3
            other_surprise = (p * 3) - 4

            if (current_sum == surprise or current_sum == other_surprise) and S > 0:
                total_googlers += 1
                S -= 1
            elif current_sum > surprise:
                total_googlers += 1

        f.write('Case #%s: %s\n' % (loop, total_googlers))
        loop += 1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        quit('python dancingwithgooglers.py <input file> <output file>')
    main(sys.argv[1], sys.argv[2])