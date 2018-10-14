
import string
import re



s = raw_input()
num_r = int(s)
c_num = 0

for r in xrange(num_r):
  c_num +=1
  s = raw_input()
  num_num = int(s)
  s = raw_input()
  nl = s.split()
  cnl = s.split()
  cnl.sort(cmp=lambda x,y: cmp(int(x),int(y)))

  wrong_count = 0

  for i in xrange(len(cnl)):
    if cnl[i] != nl[i]:
      wrong_count +=1




  p_list = []
  p_list.append("Case #")
  p_list.append(str(c_num))
  p_list.append(": ")
  p_list.append(str(wrong_count))


  print ''.join(p_list)

