#!/usr/bin/env python
def main():

    wlen, wcount, tests = [int(i) for i in raw_input().split()]

    aliendict = []
    testwords = []

    for word in range(wcount):
        aliendict.append(raw_input())

    for word in range(tests):
        testwords.append(raw_input())

    for tc in range(tests):
        count = 0
        test = testwords[tc]
        
        tw = []
        ispattern = False
        pat = ''

        for c in test:
            if c == '(':
                ispattern = True
                pat = ''
                continue
            elif c == ')':
                ispattern = False
                tw.append(pat)
                pat = ''
                continue

            if not ispattern:
                tw.append(c)
            else:
                pat = pat + c

        # got tw
        for word in aliendict:
            invalid = False
            for i in range(len(word)):
                if word[i] not in tw[i]:
                    invalid = True
                    break
            if not invalid:
                count += 1
        # output
        print 'Case #%d: %d' % (tc + 1, count)

if __name__ == '__main__':
    main()
