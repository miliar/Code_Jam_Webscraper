#!/usr/bin/env python
# coding: utf-8

import fileinput

if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        smax, ss = line.strip().split()
        friends = 0
        while True:
            applauding = friends        
            levels = [int(l) for l in ss]
            for shyness, count in enumerate(levels):
                if applauding >= shyness: 
                    applauding += count
                else:
                    friends += 1
                    break
            else:
                print('Case #%d: %d' % (i, friends))
                break
