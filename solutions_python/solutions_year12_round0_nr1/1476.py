#!/usr/bin/python
import sys
import string

def rl():
    return sys.stdin.readline().strip()

t = string.maketrans('ejpmyslckdxvnribtahwfougyqz', 'ourlangeismpbtdhwyxfckjvazq')

def main():
    T = int(rl())
    for case in range(1, T+1):
        print 'Case #%d: %s' % (case, rl().translate(t))

if __name__ == '__main__':
    main()
