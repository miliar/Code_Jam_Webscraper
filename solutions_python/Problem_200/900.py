# Python 3.5.1

from common import *

def tidy(s):
    if s == '':
        return ''

    if s[0] * len(s) <= s:
        return s[0] + tidy(s[1:])
    else:
        end = '9' * (len(s) - 1)
        if s[0] == '1':
            return end
        else:
            return str(int(s[0]) - 1) + end

def main(casenum):
    writecase(casenum, tidy(readline()))

run(main)
