def is_increasing(num):
  num_list = list(str(num))
  return all(x<=y for x, y in zip(num_list, num_list[1:]))

f = open('p2.small.in', 'r')
num_cases = int(f.readline())
for i in range(num_cases):
  num = int(f.readline())
  while not is_increasing(num):
    sub = num % 10
    num -= (sub + 1)
  print("Case #{}: {}".format(i+1, num))


