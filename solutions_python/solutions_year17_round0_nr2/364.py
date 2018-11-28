file_in = open('B-large.in')
file_out = open('B-large.out', 'w')

T = int(file_in.readline())

def is_tidy(number):
  last = 9
  while number > 0:
    if number % 10 > last: return False
    last = number % 10
    number //= 10
  return True

def tidify(number):
  temp = number
  base = 1
  t = -1
  while temp > 0:
    t = temp % 10
    if t != 9:
      return number - (t + 1) * base
    base *= 10
    temp //= 10
  return -1

for t in range(1, T+1):
  N = int(file_in.readline())

  while not is_tidy(N):
    N = tidify(N)

  file_out.write('Case #' + str(t) + ': ' + str(N) + '\n')
