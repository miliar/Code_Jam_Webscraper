import IPython

def solve(a, b):
    sum = 0
    for c in string.ascii_lowercase:
        c_in_a = a.count(c)
        c_in_b = b.count(c)
        if c_in_a > c_in_b:
            sum += c_in_a - c_in_b
    return sum

def main():
    N = input()
    for I in range(1, N + 1):
        line = raw_input()
        li = line.split()[1]
        li = map(int, li)
        standing = 0
        more = 0
        for i, n in enumerate(li):
            delta = 0
            if standing < i:
              delta = i - standing
              more += delta
            standing += n + delta

        print "Case #%s: %s" % (I, more)

if __name__ == '__main__':
    main()
