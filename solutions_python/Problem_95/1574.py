#!/usr/bin/python

import sys

before='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
after='yhesocvxduiglbkrztnwjpfmaqYHESOCVXDUIGLBKRZTNWJPFMAQ'
transMap = str.maketrans(before,after)

def solve(input):
    return input.translate( transMap )

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as f:
            n = int(f.readline())
            for i, input in enumerate(f):
                input=input.strip()
                result=solve(input)
                print('Case #{}: {}'.format(i+1,result), file=out)

