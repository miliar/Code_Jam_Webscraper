import fileinput

def isTidy(i):
    s = str(i)
    prev = "0"
    for x in s:
        if x < prev:
            return False
        prev = x
    return True

def solveBruteForce(maxVal):
    for i in range(maxVal, 0, -1):
        if isTidy(i):
            return str(i)

def main():
    it = fileinput.input()
    it.next()
    for i,l in enumerate(it):
        maxVal = int(l)
        print  "Case #%d: %s" % ( i+1, solveBruteForce(maxVal))

if __name__ == "__main__":
    main()
