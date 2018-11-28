




readfile = open("A-large.in")
writefile = open("output1.txt", "w")

lines = readfile.readlines()
#assert int(lines[0]) == len(lines) - 1

flag = 0
prob_num = 0
for line_num in xrange(1,len(lines)):
  line = lines[line_num]
  if flag == 0:
    prob_num += 1
    d,n = line.split()
    d = int(d)
    n = int(n)
    flag = 1
    my_dict = {}
  else:
    flag += 1
    k, s = line.split()
    k = int(k)
    s = int(s)
    assert not k in my_dict
    my_dict[k] = s
    if flag > n:
      flag = 0
      max_time = 0
      for k in my_dict.keys():
        time = (d - k) * 1. / my_dict[k]
        if time > max_time:
          max_time = time
      writefile.write("Case #%d: %f\n" % (prob_num, d/max_time))

writefile.close()