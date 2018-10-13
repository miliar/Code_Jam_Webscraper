import sys

def process(f):
  pass


if __name__ == '__main__':
  f = sys.stdin
  N = int(f.readline().strip())
  for n in range(N):
    row1 = int(f.readline().strip())
    cards = []
    for i in range(4):
     cards.append(f.readline().strip())
    possible1 = set(cards[row1-1].split())

    row2 = int(f.readline().strip())
    cards = []
    for i in range(4):
     cards.append(f.readline().strip())
    possible2 = set(cards[row2-1].split())

    inter = possible1 & possible2
    result = "Volunteer cheated!"
    if len(inter) > 1:
      result = "Bad magician!"
    if len(inter) == 1:
      result = inter.pop()
    print('Case #{0}: {1}'.format(n+1, result))
