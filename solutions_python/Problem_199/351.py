file_in = open('A-large.in')
file_out = open('A-large.out', 'w')

T = int(file_in.readline())

def check(pancakes):
  return ''.join(pancakes).find('-') < 0

for t in range(1, T+1):
  count = 0
  pancakes, flipper = file_in.readline().split()
  flipper = int(flipper)
  pancakes = list(pancakes)
  N = len(pancakes)
  for i in range(0, N-flipper+1):
    if pancakes[i] == '-':
      count += 1
      for j in range(flipper):
        pancakes[i+j] = ('-' if pancakes[i+j] == '+' else '+')

  file_out.write('Case #' + str(t) + ': ')
  if check(pancakes):
    file_out.write(str(count) + '\n')
  else:
    file_out.write('IMPOSSIBLE\n')
  # print(pancakes, flipper)
