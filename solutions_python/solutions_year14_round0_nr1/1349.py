
# 16 cards in a square grid
#  4 rows of cards, 4 cards per row
# each card has nubmer 1 to 16 written on it

# magician asks volunteer to choose a card and tell which row

# finally magician rranges the cards in a square grid in any order

# magician asks again which row her card is in and he determines which
#  card that the contestant chose!


input_file = open(r'/Users/JJ/Downloads/A-small-attempt0.in', 'r')
output_file = open(r'/Users/JJ/Desktop/out.txt', 'w')

t = input_file.readlines()
T = int(t.pop(0))

for case in range(T):
  n1 = int(t.pop(0))
  arrangement1 = [map(int, t.pop(0).split(' ')) for _ in range(4)]
  n2 = int(t.pop(0))
  arrangement2 = [map(int, t.pop(0).split(' ')) for _ in range(4)]

  intersection = set(arrangement1[n1-1]).intersection(arrangement2[n2-1])

  if len(intersection) == 1:
    ret = list(intersection)[0]
  elif len(intersection) > 1:
    ret = "Bad magician!"
  elif len(intersection) < 1:
    ret = "Volunteer cheated!"

  output_file.write("Case #{}: {}\n".format(case + 1, ret))

input_file.close()
output_file.close()
  
