import fileinput
import sys

def processInput():
    tcIn = fileinput.input()
    tcCount = int(tcIn.readline())
    for i in range(tcCount):
        msg = tcIn.readline()
        #if i == 3:
        print "Case #%d: %d" % (i+1, countMinSeconds(msg.strip()))

def getBase(msg):
    digits = set()
    for c in msg:
        if c not in digits:
            digits.add(c)
    return len(digits)

def getTranslation(msg):
    translation = {}
    nextDigit = 1
    weGotZero = False
    for i, c in enumerate(msg):
        if i == 0:
            translation[msg[0]] = 1
        else:
            if c in translation.keys():
                continue
            elif c != msg[0] and not weGotZero:
                translation[c] = 0
                weGotZero = True
            else:
                nextDigit += 1
                translation[c] = nextDigit
    return translation

def countMinSeconds(msg):
    base = getBase(msg)
    translation = getTranslation(msg)
    assert base == len(translation)
    #print msg, base, translation

    if base == 1:
        base = 2
    minSecs = 0
    for i, c in enumerate(msg[::-1]):
        minSecs += translation[c] * (base ** i)
    return minSecs

def main():
    processInput()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
