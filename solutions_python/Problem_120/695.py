import csv


if __name__ == "__main__":

  f = csv.reader(open('A-small-attempt0.in','r'), delimiter = ' ')
  out = open("A-small-attempt0.out","w")

  T = int(f.next()[0])

  for case in xrange(1,T+1):
    [r, t] = [int(x) for x in f.next()]
    count = 0
    n = 1
    while True:
      if 2*(n+r) - 1 <= t:
        t -= 2*(n+r) - 1
        n += 2
        count += 1
      else:
        break
    out.write("Case #%d: %s\n" % (case, count))

  out.close()
