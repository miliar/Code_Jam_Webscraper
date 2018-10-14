'''
Created on Apr 8, 2017

@author: christoph

small set version
'''

def isTidy(i):
    prev = -1
    for digit in str(i):
        if int(digit) < prev:
            return False
        prev = int(digit)
    return True

def doIt(number):
    while not isTidy(number):
        number -= 1
    return number

def main():
    T = int(raw_input())
    for i in range(T):
        inp = raw_input()
        number = int(inp)
        out = doIt(number)
        print "Case #" + str(i+1) + ": " + str(out)


if __name__ == "__main__":
    main()
