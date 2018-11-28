import random

def alter(n, i, first):
    if n[i] < n[i-1]:
        n[i] = 9
        if first:
            n[i-1] -= 1
    return n

def check_tidy(number):
    n = [int(i) for i in str(number)]
    first = True
    if sorted(n) == n:
        return n
    i = len(n) - 1
    while True:
        alter(n, i, first)
        if sorted(n) == n:
            return n
        i -= 1
        if i < 1:
            i = len(n) - 1
            first = False

def test(n):
    l = []
    for i in xrange(n+1):
        temp = [int(j) for j in str(i)]
        if sorted(temp) == temp:
            l.append(int(''.join([str(i) for i in temp])))
    return l[-1]

def main():
    # lines  = [7, 432, 203, 250, 10, 889, 319, 851]
    # lines = [line.rstrip('\n') for line in open('B-small-attempt0.in')]
    # lines = [random.randrange(10**18) for _ in xrange(3)]
    line_count = int(raw_input().strip())
    for i in xrange(line_count):
        num = int(raw_input().strip())
        temp = check_tidy(int(num))
        temp = [str(j) for j in temp]
        print "Case #%d: %d"%(i+1, int(''.join(temp)))
        # temp = [str(i) for i in temp]
        # print num, "-->", int(''.join(temp)), int(''.join(temp)) == test(int(num))
        # if int(''.join(temp)) != test(int(num)):
            # print "WRONG"

if __name__ == '__main__':
    main()
