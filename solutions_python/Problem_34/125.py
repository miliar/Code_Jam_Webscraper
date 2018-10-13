'''
Created on 2009-9-3

@author: ufo
'''
import re
def main():
    l,d,n=map(int,raw_input().split())
    known_word=[None]*d
    for i in range(d):
        known_word[i]=raw_input()
    for case in range(n):
        match=0
        pattern = raw_input().replace('(','[').replace(')',']')
        pattern='^'+pattern+'$'
        for i in range(d):
            if(re.match(pattern, known_word[i])):
                match=match+1

        print 'Case #%s: %d' % (case + 1, match)
main()