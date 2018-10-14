f = open('magic_trick_data.txt')
T = int(f.readline())
for turn in range(T):
  one = int(f.readline())
  board1 = []
  for i in range(4):
    board1.append([int(x) for x in f.readline().split()])
  two = int(f.readline())
  board2 = []
  for i in range(4):
    board2.append([int(x) for x in f.readline().split()])

  a = set(board1[one-1]).intersection(board2[two-1])
  if len(a) == 1:
    print "Case #" + str(turn+1) + ":", a.pop()
  elif len(a) > 1:
    print "Case #" + str(turn+1) + ":", "Bad magician!"
  else:
    print "Case #" + str(turn+1) + ":", "Volunteer cheated!"

