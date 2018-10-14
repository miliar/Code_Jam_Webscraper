




readfile = open("C-large.in")
writefile = open("output3.txt", "w")

lines = readfile.readlines()
assert int(lines[0]) == len(lines) - 1

for prob_num in xrange(1,len(lines)):
  line = lines[prob_num]
  n, k = line.split()
  n = int(n)
  k = int(k)
  my_dict = {n:1}
  count = 0
  while count < k:
    val = max(my_dict)
    number = my_dict.pop(val)
    min_lr = (val - 1) / 2
    max_lr = val / 2
    if min_lr in my_dict:
      my_dict[min_lr] += number
    else:
      my_dict[min_lr] = number
    if max_lr in my_dict:
      my_dict[max_lr] += number
    else:
      my_dict[max_lr] = number
    count += number
  writefile.write("Case #%d: %d %d\n" % (prob_num, max_lr, min_lr))
  print prob_num

writefile.close()