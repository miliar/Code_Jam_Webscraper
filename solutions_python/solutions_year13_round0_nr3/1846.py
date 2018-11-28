import sys

def number_fair_square(A,B):
    lower = int(A ** 0.5)
    upper = int(B ** 0.5)
    quantity = 0
    for i in xrange(lower,upper+1):
        if palindrom(i):
            square = i ** 2
            if palindrom(square) and square >= A and square <= B:
                quantity += 1
    return quantity

def palindrom(number):
    aux = number
    number_reversed = 0
    while(number > 0):
        digit = number % 10
        number_reversed = number_reversed * 10 + digit
        number = number / 10
    return aux == number_reversed

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        quantity = int(f.readline())
        for execution in xrange(quantity):
            row = f.readline()
            row = row.split()
            print 'Case #%i: %s' %(execution+1,number_fair_square(int(row[0]),int(row[1])))
