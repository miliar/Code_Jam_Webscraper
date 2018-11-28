file_in = open('B-small-attempt0.in', 'r')
file_out = open('b.out', 'w')

T = int(file_in.readline())

def can_make(ingredients, i, n):
  for j in range(n):
    if len(ingredients[j]) == 0:
      return False
    if ingredients[j][0] < i * 0.9 or ingredients[j][0] > i * 1.1:
      return False
  return True

for t in range(1, T+1):
  n, p = map(int, file_in.readline().split())

  recipe = list(map(int, file_in.readline().split()))
  ingredients = []
  for i in range(n):
    inp = file_in.readline().split()
    inp = sorted([int(n) / recipe[i] for n in inp])
    print(inp)
    ingredients.append(inp)

  i = 1
  count = 0

  while i < 1000000:
    print("loop #:{}".format(i))
    for j in range(n):
      while len(ingredients[j]) > 0 and ingredients[j][0] < i * 0.9:
        ingredients[j].pop(0)
      if len(ingredients[j]) == 0:
        i = 1000000

    while can_make(ingredients, i, n):
      for j in range(n):
        print("adding", ingredients[j].pop(0))
        if len(ingredients[j]) == 0:
          i = 1000000
      count += 1
    print(count)

    if i < 1000000:
      i = max(min(ing[0] for ing in ingredients)-10, i+1)

  file_out.write("Case #{}: ".format(t))
  file_out.write(str(count))
  file_out.write('\n')
