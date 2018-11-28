import sys

import os


maping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q'}

if __name__ == '__main__':
    fname = sys.argv[1]
    data = []
    with open(fname,'r') as fid:
        data = fid.readlines()
    data = [line.replace('\n','') for line in data]
    with open('output.txt','w') as fid:
        c = 0
        for line in data[1:]:
            line2 = ''
	    for i in range(len(line)):
                if line[i] == ' ': line2 = line2 + ' '
                else:
                    line2 = line2 + maping[line[i]]
            c += 1
            fid.write('Case #' + str(c) + ': ' + line2 + '\n')
    print 'Done'

                    
            
