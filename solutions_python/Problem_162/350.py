import numpy as np

def create():
    numbers = np.zeros(10**6+1, dtype=np.int16)
    numbers[:21] = np.arange(21)
    for i in xrange(21, 10**6+1):
        rev_i = int(str(i)[::-1])
        if rev_i < i and i % 10:
            numbers[i] = 1 + min(numbers[i-1], numbers[rev_i])
        else:
            numbers[i] = 1 + numbers[i-1]
    return numbers

def main():
    N = int(raw_input())
    numbers = create()
    for i in xrange(N):
        print "Case #{0}: {1}".format(i + 1, numbers[input()])


if __name__ == '__main__':
    main()
