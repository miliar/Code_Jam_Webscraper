number_of_cases = int(input())

def flip(pancakes, index, k):
  for i in range(k):
    pancakes[index + i] = '-' if pancakes[index + i] == '+' else '+'

for case in range(1, number_of_cases + 1):
  pancakes, k = input().split(" ")
  k = int(k)

  total_flips = 0;
  pancakes = list(pancakes)
  for i in range(len(pancakes) - k + 1):
    if pancakes[i] == '-':
      total_flips += 1
      flip(pancakes, i, k)

  is_happy = True
  for i in range(len(pancakes)):
    if pancakes[i] == '-': is_happy = False

  print("Case #{}: {}".format(case, total_flips if is_happy else 'IMPOSSIBLE'))
