file_in = open('C-large.in', 'r')
file_out = open('c.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  n, k = map(int, file_in.readline().split())

  i = k
  row = 0
  while i > 1:
    i //= 2
    row += 1

  p = pow(2, row)

  sum_row = n - p + 1
  col = k - p + 1

  target = sum_row // p + (col <= sum_row % p)

  file_out.write("Case #{}: ".format(t))
  file_out.write("{} {}".format(target // 2, (target - 1) // 2))
  file_out.write('\n')