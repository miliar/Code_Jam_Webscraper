t = int(input())

def flip(pancakesIn, flipper):
    pancakes = list(pancakesIn)
    count = 0
    while True:
        if pancakes.count('-') == 0:
            return count
        if (len(pancakes) - pancakes.index('-')) < flipper:
            return 'IMPOSSIBLE'

        for i in range(pancakes.index('-'), pancakes.index('-')+flipper):
            if pancakes[i] == '-':
                pancakes[i] = '+'
            elif pancakes[i] == '+':
                pancakes[i] = '-'

        count += 1
    return count

for i in range(1, t + 1):
  n, m = [str(s) for s in input().split(" ")]
  q = int(m)
  a = flip(n, q)
  print("Case #{}: {}".format(i, a))
