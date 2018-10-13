file_in = None
def raw_input(s_filename=''):
  if s_filename == '':
    s_filename = 'A-small-attempt0.in.txt'
  global file_in
  if file_in == None: 
    file_in = open(s_filename)
  try:
    return file_in.next()
  except:
    file_in = open(s_filename)
    return file_in.next()

t = int(raw_input())
for i in range(1, t+1):
  n, m = raw_input().split(' ')
  print i, n, m
#----begin the prob-----

def flip_bit(_s, _mask):#mask is all one at given range
  _part_remain = _s & ~_mask
  _part_flip = _s & _mask
  _flippen = ~_part_flip & _mask
  return _part_remain | _flippen

def create_mask(_l, _r):
  return ~(~((1 << _r) - 1) | ((1 << _l) - 1))

def transform(_text):
  result = 0
  for i, c in enumerate(_text):
    if _text[i] == '+':
      result = result | 1 << i
  return result

def is_finish(_bin, _L):
  binlen = 0
  count = 0
  for i in range(_L):
    binlen += 1
    if (1 << i) & _bin == (1 << i):
      count += 1
  if binlen == count:
    return True
  else:
    return False

def unit_test():
  _text = '--++----+-'
  _bin = transform(_text)
  _mask = create_mask(3, 8)
  _bin2 = flip_bit(_bin, _mask)
  print bin(_bin)
  print bin(_bin2)
  print is_finish(_bin)
  print is_finish(_bin2)



def expand_node(_bin, _K, _L, verbose=False):
  result = []
  for i in range(_L - _K + 1):
    _mask = create_mask(i, i+_K)
    temp = flip_bit(_bin, _mask)
    if verbose == True:
      print '#iter: ', i
      print 'org: ', _bin
      print 'mask: ', bin(_mask)
      print 'flipped: ', bin(temp)
    result.append(temp)
  return result

def expand_lvl(_node_list, _K, _L, _lvl=0, verbose=False):
  result = []
  for node in _node_list:
    temp = expand_node(node, _K, _L)
    for item in temp:
      if is_finish(item, _L) == True:
        return True, item
    result.extend(temp)

  return False, result

def solve(_s, _K, verbose=False):
  _root = transform(_s)
  L = len(_s)

  if is_finish(_root, L) == True:
    return True, 0
  Q = [_root]
  found = False
  step = 1
  expanded_node_list = set()
  while found == False and Q != set([]) and step < 16:
    if verbose==True:
      print 'step: {}\nopened nodes: {}'.format(step, Q)

    found, P = expand_lvl(Q, _K, L, step)
    if found == True:
      return True, step
    R = set()
    for node in P:
      if node not in expanded_node_list:
        R.add(node)
        expanded_node_list.add(node)
    Q = R 
    step = step + 1
  return False, step

def solve_all(s_filename):
  global file_in
  file_in = None
  with open('output.txt', 'w') as file_out:
    t = int(raw_input(s_filename))
    for i in range(1, t+1):
      s, K = raw_input().split(' ')
      K = int(K)
      result, item = solve(s, K)
      file_out.write('Case #{}: {}\n'.format(i, item if result==True else 'IMPOSSIBLE'))    
    
  

	





