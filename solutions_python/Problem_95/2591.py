from __future__ import print_function
import string
import sys

table = string.maketrans(string.ascii_lowercase, 'yhesocvxduiglbkrztnwjpfmaq')

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        G = sys.stdin.readline()
        print('Case #%d: '%(i+1)+string.translate(G, table), end='')
