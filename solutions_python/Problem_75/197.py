
import string
import re


s = raw_input()
cases = int(s)
c_num = 0
for countr in xrange(cases):
  c_num += 1
  s = raw_input()
  inp = s.split()
  c = int(inp[0])

  c_d = {}
  for i in range(1,1+c):
    st = inp[i]
    l1 = st[0]
    l2 = st[1]
    cl = st[2]
    ls = frozenset((l1, l2))
    c_d[ls] = cl

  d = int(inp[1+c])
  d_d ={}
  for i in range(2+c, 2+c+d):
    st = inp[i]
    l1 = st[0]
    l2 = st[1]
    if l1 in d_d:
      d_d[l1].add(l2) 
    else:
      d_d[l1] = set(l2)

    if l2 in d_d:
      d_d[l2].add(l1) 
    else:
      d_d[l2] = set(l1)

  num_letters = int(inp[2+c+d])
  letters = inp[3+c+d]

  let_list = []
  count = {}
  for let in letters:
    if not let_list:
      let_list.append(let)
      if let in count:
        count[let] += 1
      else:
        count[let] = 1
    else:
      letset = frozenset((let,let_list[-1]))
      processed = False
      if letset in c_d:
        old_let = let_list.pop()
        count[old_let] -= 1

        new_let = c_d[letset]
        let_list.append(new_let)
        if new_let in count:
          count[new_let] += 1
        else:
          count[new_let] = 1
        processed = True

      elif let in d_d:
        del_set = d_d[let]
        for key, val in count.items():
          if val > 0:
            if key in del_set:
              processed = True
              count = {}
              let_list = []

      
      if not processed:
        let_list.append(let)
        if let in count:
          count[let] += 1
        else:
          count[let] = 1
          
  p_list = []
  p_list.append("Case #")
  p_list.append(str(c_num))
  p_list.append(": [")
  for let in let_list:
    p_list.append(let)
    p_list.append(", ")
  if let_list:
    p_list.pop()
  p_list.append("]")
  p = ''.join(p_list)
  print p


