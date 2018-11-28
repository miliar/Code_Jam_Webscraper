




readfile = open("B-small-attempt0.in")
writefile = open("output2.txt", "w")

lines = readfile.readlines()
#assert int(lines[0]) == len(lines) - 1

flag = 0
#prob_num = 0
for prob_num in xrange(1,len(lines)):
  line = lines[prob_num]
  ret = [int(x) for x in line.split()]
  n = ret[0]
  vals = ret[1:]
  print n, vals
  assert(sum(vals) == n)
  #easy case:
  #if 2*max(vals) > sum(vals):
    #writefile.write("Case #%d: IMPOSSIBLE\n" % (prob_num))
  #else:
  answer = ""
  char_LU = ['R', 'O', 'Y', 'G', 'B', 'V']
  fake_vals = []
  for i in xrange(3):
    fake_vals.append( vals[2*i] - vals[(2*i+3)%6])
  if (min(fake_vals) < 0) or (2*max(fake_vals) > sum(fake_vals)):
    writefile.write("Case #%d: IMPOSSIBLE\n" % (prob_num))
  else:
    max_i = -1
    max_v = 0
    initial_char = -1
    for i in xrange(3):
      if max_v < fake_vals[i]:
        max_v =  fake_vals[i]
        max_i = i
        initial_char = i
    while sum(fake_vals) > 0:
      answer += char_LU[2*max_i]
      fake_vals[max_i] -= 1
      old_max_i = max_i
      max_i = -1
      max_v = 0
      for i in xrange(3):
        if i != old_max_i:
          if fake_vals[i] > max_v or (fake_vals[i] >= max_v and i == initial_char):
            max_v =  fake_vals[i]
            max_i = i
    for i in [1,3,5]:
      if vals[i] > 0:
        if answer != '':
          pos = answer.index(char_LU[(i+3)%6])
          add_string = (char_LU[(i+3)%6] + char_LU[i%6]) * vals[i]
          answer = answer[:pos] + add_string + answer[pos:]
        else:
          answer = (char_LU[(i+3)%6] + char_LU[i%6]) * vals[i]
    writefile.write("Case #%d: %s\n" % (prob_num, answer))

writefile.close()