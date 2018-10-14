'''
Created on Sep 2, 2009

@author: Isabelle
'''

import sys

def main():
    input = open('A-large.in')
        
    info = input.readlines()
    input.close()
    info[0] = map(int, info[0].split())
    (L, D, N) = info[0]
    diction = [d.strip('\n') for d in info[1:(1+D)]]
        
    def getLetter(k, w, word, valid):
        c = 0
        for a in range(0,len(word[k])):
            wd = w + word[k][a]
            if k < L-1:
                new_valid = [v for v in valid if v.startswith(wd)]
                if new_valid == []: continue
                c += getLetter(k+1, wd, word, new_valid)
            elif wd in valid:
                c += 1
        return c
    
    output = open('A-large.out', 'w')
    
    for x in range(1+D,len(info)):
        test = info[x]
        test = test.strip('\n')
        word = []
        i = 0
        while i < len(test):
            if test[i] == '(':
                word.append(test[test.index('(',i)+1:test.index(')',i)])
                i = test.index(')',i)+1
            else:
                word.append(test[i])
                i += 1
        valid = [d for d in diction]
        count = getLetter(0, '', word, valid)
        
        output.write('Case #' + str(x-D) + ': ' + str(count) + '\n')
        
    output.close()
    

if __name__ == '__main__':
    sys.exit(main())
    