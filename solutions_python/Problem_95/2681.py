import sys

def main():
    alphabet = buildAlphabet()
    inputFile = open('A-small-attempt1.in', 'rU')
    lines = inputFile.readlines()
    n = int(lines.pop(0))
    for i in range(len(lines)):
        clearLine = ''
        for c in lines[i]:
            clearLine += alphabet[c]
        print 'Case #' + str(i + 1) + ': ' + clearLine,

def buildAlphabet():
    cipherFile = open('cipher_text.txt', 'rU')
    clearFile = open('clear_text.txt', 'rU')
    cipherText = cipherFile.read()
    clearText = clearFile.read()
    alphabet = {}
    alphabet['z'] = 'q'
    alphabet['q'] = 'z'
    for i in range(0, len(cipherText)):
        alphabet[cipherText[i]] = clearText[i]
    return alphabet

if __name__ == '__main__':
  main()
