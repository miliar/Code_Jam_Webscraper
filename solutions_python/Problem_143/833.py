#!/usr/bin/python

# Dan Seminara

import fileinput

def main():
    for i,line in enumerate(fileinput.input()):
        if i == 0:
            continue
        [a_s,b_s,k_s] = [int(x) for x in line.strip().split(' ')]
        total = a_s+b_s-1
        for k in range(k_s):
            for a in range(1,a_s):
                for b in range(1,b_s):
                    if a&b == k:
                        total += 1
        print('Case #%d: %d' % (i,total))

            
if __name__ == '__main__':
    main()