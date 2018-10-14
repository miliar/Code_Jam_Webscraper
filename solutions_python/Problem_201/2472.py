import functools
import math
import sys


class LastTidy:


  def run(n):
    s = str(int(n))
    l = list(s)
    f_i = 0
    f_d = int(s[f_i])
    for i in range(f_i, len(s)-1):
      assert f_d != 0
      print(i, f_i, f_d, s[i+1])
      if int(s[i+1]) > f_d:
        f_i = i+1
        f_d = int(s[f_i])
        continue
      elif int(s[i+1]) == f_d:
        continue
      else:
        print('hi')
        f_d -= 1
        l[f_i] = str(f_d)
        l[f_i+1:] = ['9' for _ in range(len(s)-1-f_i)]
        break
    return (int(''.join(l)),)


  def test(n, answer):
    def v(x):
      x = list(str(x))
      for i in range(len(x)-1):
        if int(x[i]) > int(x[i+1]):
          return
      raise Exception((n, answer))
    answer += 1
    while answer < n+1:
      if v(answer):
        print(n, answer)
        raise Exception('bad tidy')
      answer += 1


class Broom:

  def run(n, k):
    n, k = int(n), int(k)

    # checky mc_check
    if n >= k and n > 0 and k > 0:
      pass
    else:
      return ('IMPOSSIBLE',)

    tree = {
      0: ('space', n)
    }
    pq = [(0, n)]
    peeps = []

    def pq_ins(space):
      for i in range(len(pq)):
        if pq[i][1] < space[1]:
          pq[i:i] = [space]
          return
        elif pq[i][1] == space[1] and space[0] < pq[i][0]:
          pq[i:i] = [space]
          return
        else:
          continue
      pq.append(space)

    for i in range(k):

      try:
        top, *pq = pq
      except:
        print(pq)
      lpos, size = top

      if tree[lpos][0] != 'space':
        print(tree)
        raise Exception('here')

      del tree[lpos]

      rpos = lpos + size - 1
      ppos = (lpos + rpos) // 2

      person = ('person', ppos - lpos, rpos - ppos)
      tree[ppos] = person
      peeps.append(person)

      if rpos - ppos >= 1:
        n_space = rpos - ppos
        space = ('space', n_space)
        pq_space = (ppos+1, n_space)
        tree[ppos+1] = space
        pq_ins(pq_space)
        print(pq)

      if ppos - lpos >= 1:
        n_space = ppos - lpos
        space = ('space', n_space)
        pq_space = (lpos, n_space)
        tree[lpos] = space
        pq_ins(pq_space)
        print(pq)


    print(peeps)
    print(tree)

    l_s, r_s = peeps[-1][1:]

    return max(l_s, r_s), min(l_s, r_s)


  def test(n, k, l_s, r_s):
    ...






TEST = True

m = Broom

if len(sys.argv) > 2 and sys.argv[1] == '1off' and TEST:
  args = sys.argv[2:]
  answer = m.run(*args)
  print(*answer)
  m.test(*args, *answer)

elif len(sys.argv) == 2:
  f = open(sys.argv[1])
  out = open(sys.argv[1].replace('.in', '.out'), 'w')
  next(f)
  for i, l in enumerate(f):
    args = l.split()
    answer = m.run(*args)
    out.write('Case #{}: {}\n'.format(i+1, ' '.join(str(a) for a in answer)))
    if TEST:
      m.test(*args, *answer)
  out.close()
  f.close()
