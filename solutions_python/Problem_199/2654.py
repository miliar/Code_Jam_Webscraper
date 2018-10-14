def isSorted(n):

    return n == '+' * len(n)

def swap(n, k):
    a = ''
    try:
        for i in range(k):
            if n[i] == '-':
                a += '+'
            else: a += '-'

        a += n[k:]
        return a
    except:
        return 'IMPOSSIBLE'

def calculate(n, k):

    i = 0
    while not isSorted(n):
        m = n.find('-')
        n = n[m:]
        n = swap(n, k)
        i += 1
        if n == 'IMPOSSIBLE':
            return n
    return i

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = raw_input().split()  # read a list of integers, 2 in this case
  n = calculate(n, int(k))
  print "Case #{}: {} ".format(i, n)
  # check out .format's specification for more formatting options
