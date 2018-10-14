# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def std_ovation(file):
    with open(file,'r') as ifile:
        case = int(ifile.readline())
        with open('output.txt', 'w') as wfile:
            for i in range(case):
                line = ifile.readline()
                max_shy, sequence = line.split()
                max_shy = int(max_shy)
                audience = [int(k) for k in sequence]
                total = 0
                take = 0
                for shy_level in range(max_shy):
                    if shy_level == 0:
                        if audience[0] == 0:
                            take += 1
                            total += take
                        else:
                            total += audience[0]
                    else:
                        current_adu = audience[shy_level]
                        if total + current_adu > shy_level:
                            total += current_adu
                        else:
                            take += 1
                            total = total+current_adu+ 1
                wfile.write('Case #{0}: {1}\n'.format(i+1, take))
        
                        
                        

if __name__ == '__main__':
	import sys
	file = sys.argv[1]
	std_ovation(file)