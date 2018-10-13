#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

from math import sqrt

def opn():
    #return open('A-test.in.txt'), open('A-test.out', 'w')
    #return open('A-small-attempt0.in.txt'), open('A-small.out', 'w')
    return open('A-large.in.txt'), open('A-large.out', 'w')


def main():
    
    f1, f2 = opn()

    runs = int(f1.readline()[:-1])

    for run in range(runs):
    
        line = f1.readline()[:-1]
        perkey, numkeys, numletters = [int(i) for i in line.split()]
        numbers = [int(i) for i in (f1.readline()[:-1]).split()]
        
        numbers.sort()
        presses = 1
        total = 0
        keysfilled=0
        for i in reversed(numbers):
            total += i*presses
            keysfilled += 1
            if keysfilled == numkeys:
                presses += 1
                keysfilled = 0


        print >> f2, "Case #%d: %d" % (run+1, total)
        print "Case #%d: %d" % (run+1, total)

    
    f2.close()
    f1.close()






if __name__ == '__main__':
    main()
