#!/usr/bin/python

import sys
import itertools

vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def find_n_consonant_substring(name, n):
    count = 0
    for i in xrange(len(name)):
        for j in xrange(i+n-1,len(name)):
            substring = name[i:j+1]
            nn=0
            for k in xrange(len(substring)):
                if substring[k] in vowels:
                    if nn>=n:
                        break
                    nn=0
                else:
                    nn+=1
            if nn>=n:
                count+=1
    return count

def main():
    n_cases = int(sys.stdin.readline())
    for i in xrange(1,n_cases+1):
        lawn=[]
        name,n=sys.stdin.readline().strip().split(' ')
        count = find_n_consonant_substring(name,int(n))
        print 'Case #{0}: {1}'.format(i, count)

if __name__ == '__main__':
    main()
