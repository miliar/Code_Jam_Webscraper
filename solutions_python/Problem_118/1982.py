# Joseph Lee <gengarkhan@gmail.com>
# codejam 2013 - Problem C

def palindrome(num):
    numStr = str(num)
    for i in xrange(len(numStr) / 2):
        #print numStr[i], numStr[-1 - i]
        if numStr[i] != numStr[-1 - i]:
            return False
    return True

def fair_and_square(nums):
    count = 0
    for num in nums:
        if palindrome(num):
            sqroot = num ** 0.5
            if (sqroot.is_integer() and 
                    palindrome(int(sqroot))):
                count += 1
    return count

def main(arg):
    with open(arg, 'r') as infile:
        data = infile.readlines()
    data.pop(0)
    count = 1
    while len(data) > 0:
        a, b = map(int, data.pop(0).strip().split(' '))
        print 'Case #%d: %d' % (
                count, fair_and_square(range(a, b + 1)))
        count += 1
    

if __name__ == '__main__':
    from sys import argv
    main(argv[1])
