#!/usr/bin/env python
"""
usage: python welcome.py < C-small/large.in
"""

WORDS = 'welcome to code jam'

def do_clean(teststring):
    cleaned = ''
    for char in teststring:
        if char in WORDS:
            cleaned += char
    return cleaned

def calculate(mystring, windex=0, start=0):
    count = 0

    while True:
        index = mystring.find(WORDS[windex], start)
        if index == -1:
            break
        if windex == len(WORDS) - 1:
            count += 1
            start = index + 1
            continue

        count += calculate(mystring, windex + 1, index + 1)
        start = index + 1
    return count

def main():
    for casenum in range(input()):
        teststring = raw_input()
        cleanstring = do_clean(teststring)
        cleanstring = cleanstring[cleanstring.find('w'):]

        res = calculate(cleanstring) % 10000

        ret = ''
        if res < 1000:
            ret += '0'
        if res < 100:
            ret += '0'
        if res < 10:
            ret += '0'
        ret += str(res)
        print 'Case #%d: %s' % (casenum + 1, ret)

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main()
