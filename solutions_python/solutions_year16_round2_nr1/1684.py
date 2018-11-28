#!/usr/bin/env python

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
MEMO = {'': ''}

def pre(numbers):
    keys = []
    for num in numbers:
        for letter in num:
            if letter not in keys:
                keys.append(letter)
    keys.sort()
    return keys

KEYS = pre(NUMBERS)

def lettersCountToKey(lettersCount):
    theKey = ''
    for key in KEYS:
        if lettersCount.get(key, 0) != 0:
            theKey += key + str(lettersCount[key])
    return theKey

def digits(strDigits):
    lettersCount = {}
    for letter in strDigits:
        lettersCount[letter] = lettersCount.get(letter, 0) + 1
    return _digits(lettersCount, 0)

def _digits(lettersCount, d):

    theKey = lettersCountToKey(lettersCount)
    ans = MEMO.get(theKey, None)
    if ans != None:
        return ans

    for i in range(d, 10):
        strNum = NUMBERS[i]
        for letter in strNum:
            lettersCount[letter] = lettersCount.get(letter, 0) - 1

        isValid = True
        for letter in strNum:
            if lettersCount[letter] < 0:
                isValid = False
        if isValid == False:
            for letter in strNum:
                lettersCount[letter] += 1
        else: #valid
            res = _digits(lettersCount, i)
            for letter in strNum:
                lettersCount[letter] += 1
            if res != False:
                MEMO[theKey] = str(i) + res
                return str(i) + res

    MEMO[theKey] = False
    return False




T = int(raw_input().strip())
for testCaseNo in range(T):

    strDigits = raw_input().strip()

    print 'Case #' + str(testCaseNo + 1) + ':',
    print digits(strDigits)