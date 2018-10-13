'''
Created on 14-Apr-2012

@author: dushyant
'''

I = ["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"]
O = ["our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"]
MAP = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','q':'z','z':'q'}
import sys

def findMap(I, O, mapping):
    
    for i in range(len(I)):
        mapping[I[i]] = O[i]
        
    print O

def convert(I, mapping):
    O = []
    for i in range(len(I)):
        O.append(mapping[I[i]])
    return ''.join(O)

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        sys.stdout.write("Case #%d: %s\n"%(i+1,convert(sys.stdin.readline().strip(), MAP)))
    
if __name__ == '__main__':
    main()