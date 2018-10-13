
if __name__ == "__main__":
  # read input
  t = int(raw_input())
  for i in xrange(1, t + 1):
    number = raw_input()
    number = list(number)
    length = len(number)
    for c in xrange(0, length-1):
        cur = length-1-c
        #print(number[cur])
        if (int(number[cur]) < int(number[cur-1])):
             for j in xrange(cur, length):
                 number[j] = '9'
             number[cur-1] = '0' if number[cur-1] == '0' else str(int(number[cur-1]) - 1)
    last_number = int(''.join(number))
    print "Case #{}: {}".format(i, last_number)
