import fileinput

def parse(challenge):
  cases = int(challenge[0])
  assert(len(challenge) == cases + 1)
  return [
      map(float, case.split())
      for case in challenge[1:]
      ]


# is there a closed form? yes? k thx bye!
def guess(C, F, X):
  r = 2
  t = 0
  yolo = None
  swag = None
  while swag is None or swag > yolo:
    swag = yolo
    a = X / float(r)
    b = C / float(r)
    r += F
    yolo = a+t
    t += b
  return round(swag, 7)

Q = parse([line.strip() for line in fileinput.input()])
for index, question in enumerate(Q):
  print 'Case #%d: %.7f' % (index+1, guess(*question))
