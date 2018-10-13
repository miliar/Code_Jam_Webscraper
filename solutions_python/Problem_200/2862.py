def isSorted(n):

    if len(n) == 1:
        return True

    return n[0] <= n[1] and isSorted(n[1:])


def rectificate(n):

    i = 0
    while i < len(n) -1:
        if n[i] > n[i+1]:
            n = n[:i] + str(int(n[i]) - 1) + '9' * len(n[i+1:])
        i+=1

    return n


def calculate(n):

    while not isSorted(n):
        n = rectificate(n)

    return str(int(n))

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()  # read a list of integers, 2 in this case
  n = calculate(n)
  print "Case #{}: {} ".format(i, n)
  # check out .format's specification for more formatting options
