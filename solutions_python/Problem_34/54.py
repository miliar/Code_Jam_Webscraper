'''
Created on Sep 3, 2009
@author: namnx
'''
import string
import re
INFILE = 'alien-large.in'
OUTFILE = 'alien-large.out'


def main():
    fin = file(INFILE, 'r')
    fout = file(OUTFILE, 'w')
    s = fin.readline().split()
    l = int(s[0])
    d = int(s[1])
    n = int(s[2])
    words = []
    for i in range(0, d):
        words.append(fin.readline().strip())
        
    for i in range(0, n):
        message = fin.readline().strip()
        matched = countMatched(message, words)
        fout.write('Case #' + str(i+1) + ': ' + str(matched) + '\n')
        
    fin.close()
    fout.close()
    return 


def countMatched(message, words):
    message = message.replace('(', '[')
    message = message.replace(')', ']')
    p = re.compile(message)
    count = 0
    for word in words:
        if p.match(word): 
            count += 1
    print count
    return count

if __name__ == '__main__':
    main()

