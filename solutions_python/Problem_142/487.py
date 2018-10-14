def main():
  f = open('A.in', 'r')
  T = int (f.readline())

  for t in range(1, T+1):
    print 'Case #' + str(t) + ':',
    solve(f)

def solve(f):
    N = int (f.readline())
    s = []
    for n in range(0, N):
      s.append(f.readline().rstrip())
    letters = getLetters(s[0])
    numbers = []
    # check if possible
    for line in s:
      if (not getLetters(line) == letters):
        print 'Fegla Won'
        return
      numbers.append(getNumbers(line))
    # if possible
    print calculate(numbers)

def getLetters(l):
  x = [l[0]]
  for c in l[1:]:
    if (c != x[-1]):
      x.append(c)
  return x

def getNumbers(l):
  x = [1]
  last = l[0]
  for c in l[1:]:
    if (c == last):
      x[-1] += 1
    else:
      last = c
      x.append(1)
  return x

def calculate(num):
  # transpose
  n = zip(*num)
  s = 0
  for a in n:
    average = avg(a)
    for x in a:
      s += abs(average - x)
  return s

def avg(l):
  return int(round(reduce(lambda x, y: x + y, l) / float(len(l))))

if __name__ == "__main__":
    main()
