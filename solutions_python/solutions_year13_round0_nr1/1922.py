positions = [
  [0,1,2,3],
  [4,5,6,7],
  [8,9,10,11],
  [12,13,14,15],
  [0,4,8,12],
  [1,5,9,13],
  [2,6,10,14],
  [3,7,11,15],
  [0,5,10,15],
  [3,6,9,12]
]
answers = [
  'O won',
  'X won',
  'Game has not completed',
  'Draw'
]

def main():
  n = int(input())
  for i in range(n):
    draw = True
    p = -1
    matrix = ""
    for j in range(4):
      matrix = "".join([matrix, raw_input()])

    for pos in positions:
      substring = [matrix[x] for x in pos]
      if '.' not in substring:
        if 'X' not in substring:
          p = 0
          break
        elif 'O' not in substring:
          p = 1
          break
      else:
        draw = False

    # checking if p has been defined
    if p == -1:
      if draw:
        p = 3
      else:
        p = 2

    print 'Case #%s: %s' % (i + 1, answers[p] )
    
    try:
      extra = raw_input()
    except Exception, e:
      pass
main()