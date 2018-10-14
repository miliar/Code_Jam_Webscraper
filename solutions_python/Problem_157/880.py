#### Template. Destription ####

# from math import sqrt, ceil, floor


# input
filename = "input"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')
tbl = {'1' : {'1':'1', 'i': 'i', 'j': 'j', 'k': 'k',},
       'i' : {'1':'i', 'i':'-1', 'j': 'k', 'k':'-j',},
       'j' : {'1':'j', 'i':'-k', 'j':'-1', 'k': 'i',},
       'k' : {'1':'k', 'i': 'j', 'j':'-i', 'k':'-1',}}


def sign(x):
  assert 0<len(x)<3
  return -1 if len(x)==2 else 1

def abs(x): 
  assert 0<len(x)<3
  return x[1] if len(x)==2 else x 

def mult(a,b):
  s = sign(a) * sign(b)
  v = tbl[abs(a)][abs(b)]
  return v if s==1 else ('-' + v if len(v)==1 else v[1])

def peek(x):
  if len(x) == 0:
    return None
  else:
    return x[len(x)-1]


# test case loop
for caseIdx in range(T):
    [L, X] = map(int, lines.__next__().split(' '))
    s = lines.__next__()
    s = s * X

    # sl = split left, sr = split right
    # a \in sl, b \in sr ==> [0,a] (a,b) [b,len(s)-1]
    sl = []
    sr = []

    x = '1'
    for i in range(len(s)):
      x = mult(x,s[i])
      if x == 'i':
        sl.append(i)

    sl.reverse()

    x = '1'
    for i in reversed(range(len(s))):
      x = mult(s[i], x)
      if x == 'k':
        sr.append(i)

    splittable = False
    cand = set()
    for i in range(len(s)):
      if peek(sr) == i:
        sr.pop()
        if 'j' in cand:
          splittable = True
          break

      cand = set(map(lambda x: mult(x, s[i]), cand))

      if peek(sl) == i:
        sl.pop()
        cand.add('1')

    # print output
    msg = "YES" if splittable else "NO"
    out = 'Case #' + str(caseIdx + 1) + ': ' + msg + '\n'
    output.write(out)
    # print(out)

output.close()
print(open('output', 'r').read())
