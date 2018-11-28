import sys

def main():
  cin = sys.stdin
  T = int(cin.readline())
  for t in xrange(T):
    print 'Case #' + str(t+1) + ':',
    num = int(cin.readline())
    data = cin.readline().split()

    data = map(lambda x: int(x), data)

    bitsum = 0
    for x in data:
      bitsum ^= x
    if bitsum != 0:
      print 'NO'
    else:
      data = sorted(data)
      print sum(data) - data[0]

if __name__ == '__main__':
  main()
