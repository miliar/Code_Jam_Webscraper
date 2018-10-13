#!/usr/bin/env pypy

import sys

# Bit shift direction for negative sign
# ij -> 01 10 --> 01 >> 1

# Binary XOR for result
# ii -> -1
# ij -> k       (01 ^ 10 ->  11)
# ik -> -j      (01 ^ 11 -> -10)
# ji -> -k
# jk -> i       (10 ^ 11 ->  01)
# 

# ijk -> ij k -> k k -> -1

#

mapping = {
    '1': {
        '1': '1',
        'i': 'i',
        'j': 'j',
        'k': 'k'
    },
    'i': {
        '1': 'i',
        'i': '-1',
        'j': 'k',
        'k': '-j'
    },
    'j': {
        '1': 'j',
        'i': '-k',
        'j': '-1',
        'k': 'i',

        '-1': '-j',
        '-i': 'k',
        '-j': '1',
        '-k': '-i',
    },
    'k': {
        '1': 'k',
        'i': 'j',
        'j': '-i',
        'k': '-1',

        '-1': '-k',
        '-i': '-j',
        '-j': 'i',
        '-k': '1'
    },

    '-1': {
        '1': '-1',
        'i': '-i',
        'j': '-j',
        'k': '-k',

        '-1': '1',
        '-i': 'i',
        '-j': 'j',
        '-k': 'k'
    },
    '-i': {
        '1': '-i',
        'i': '1',
        'j': '-k',
        'k': 'j',

        '-1': 'i',
        '-i': '-1',
        '-j': 'k',
        '-k': '-j'
    },
    '-j': {
        '1': '-j',
        'i': 'k',
        'j': '1',
        'k': '-i',

        '-1': 'j',
        '-i': '-k',
        '-j': '-1',
        '-k': 'i',
    },
    '-k': {
        '1': '-k',
        'i': '-j',
        'j': 'i',
        'k': '1',

        '-1': 'k',
        '-i': 'j',
        '-j': '-i',
        '-k': '-1'
    }
}

def mul(i, j): return mapping[i][j]

letters = {
    0: 'i',
    1: 'j',
    2: 'k'
}
def convertToAlpha(mapping, letter, l):
    return l if mapping[letter] % 2 != 0 else '1'
    
def canContinue(count, letter, l):
    result = mul(
                mul(convertToAlpha(count, 0, l), convertToAlpha(count, 1, l)),
                convertToAlpha(count, 2, l))
    return result in (l, '-' + l)

with file(sys.argv[1]) as inFile:
    testCases = int(inFile.readline())
    for testCase in range(1, testCases + 1):
        L, X = [ int(i) for i in inFile.readline().split() ]
        combo = inFile.readline().split()[0]
        combo = combo * X

        if len(combo) < 3:
            print 'Case #%d: NO' % (testCase)
            continue

        found = False

        I, J, K = range(0, 3)
        firstCount = [0, 0, 0]
        secondCount = [0, 0, 0]
        thirdCount = [0, 0, 0]

        first = ''
        second = ''
        third = ''

        productFirst = '1'
        productSecond = '1'
        productThird = '1'

        secondBegin = ''
        thirdBegin = ''

        cacheSecond = {}
        cacheThird = {}

        comboLen = len(combo)
        for ix in range(0, comboLen):
            if comboLen < 3:
                break

            if found:
                break

            if secondBegin == '':
                first = combo[ : ix + 1]
                productFirst = reduce(lambda x, y: mul(x, y), first)
            else:
#               first += secondBegin
                productFirst = mul(productFirst, secondBegin)

            if productFirst != 'i':
                continue

                second = ''

            for jx in range(ix + 1, comboLen):

                kx = jx + 1
                if kx >= comboLen:
                    break

                i = combo[ix]
                j = combo[jx]
                k = combo[kx]

                if second == '':
                    second = combo[ix + 1 : kx]

                    secondBegin = j

                    productSecond = reduce(lambda x, y: mul(x, y), second)
                    if kx in cacheThird:
                        productThird = cacheThird[kx]
                    else:
#                       third = combo[kx:]
                        productThird = reduce(lambda x, y: mul(x, y), combo[kx:])    # expensive
                        cacheThird[kx] = productThird

                else:
#                   second += thirdBegin
                    productSecond = mul(productSecond, thirdBegin)

#                   third = third[1:]
                    productThird = mul(mul('-1', thirdBegin), productThird)
                    cacheThird[kx] = productThird

                thirdBegin = k

#               print '%s (%s)  ->  %s (%s)  ->  %s (%s)' % (
#                   first, productFirst,
#                   second, productSecond,
#                   third, productThird)

                if (productFirst, productSecond, productThird) == ('i', 'j', 'k'):
#                   print first, second, third
                    found = True
                    break

        print 'Case #%d: %s' % (testCase, 'YES' if found else 'NO')
