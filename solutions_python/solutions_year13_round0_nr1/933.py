#!/usr/bin/env python
#author: Chen Zhao

import os.path

finput = '/Users/chin/dev/codejam/test.input'
finput = '/Users/chin/dev/codejam/2013/A-small-attempt0.in'
finput = '/Users/chin/dev/codejam/2013/A-large.in'

def win(char4):
    if type(char4)==list:
        char4 = ''.join(char4)
    clean = char4.replace('T', '')
    if '.' in clean:
        return '.'
    if ('X' in clean and not 'O' in clean):
        return 'X'
    if ('O' in clean and not 'X' in clean):
        return 'O'
    return ''

def solve(data):
    to_test = [line[:] for line in data]

    for i in range(4):
        to_test.append([l[i] for l in data])
    to_test.append([data[i][i] for i in range(4)])
    to_test.append([data[3-i][i] for i in range(4)])
    no_complete = False
    for t in to_test:
        r = win(t)
        if r=='.':
            no_complete = True
            continue
        if r:
            return '%s won'%(r)
    else:
        return 'Game has not completed' if no_complete else 'Draw'

        
    

def main():
    f = file(finput)
    N = int(f.readline())
    for i in range(1, N+1):
        data = [f.readline().strip() for x in range(4)]
        print 'Case #%d: %s'%(i, solve(data))
        f.readline()
    pass

if __name__=='__main__':
    main()

