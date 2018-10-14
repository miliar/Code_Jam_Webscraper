# dynamic programming
# from pos i
# w_0 w_1 ... w_i ... w_18

# 1000 999
# 11111001001 999
# 89999
# 98808

for t in range(1, input() + 1):
  i = input()
  def tidy(i):
    return str(i) == ''.join(sorted(str(i)))

  def borrow_from(str_i, idx):
    assert idx != 0
    str_i = list(str_i)
    for i in range(idx, len(str_i)):
      str_i[i] = '9'
    while str_i[idx - 1] == '0':
      assert idx != 0
      str_i[idx - 1] = '9'
      idx -= 1
    str_i[idx - 1] = str(int(str_i[idx - 1]) - 1)
    return ''.join(str_i)

  while not tidy(i):
    str_i = str(i)
    for digit_idx in range(len(str_i) - 1, 0, -1):
      if str_i[digit_idx] < str_i[digit_idx-1]:
        str_i = borrow_from(str_i, digit_idx)
        break
    i = int(str_i)
  print "Case #%d: %d" % (t, i)
