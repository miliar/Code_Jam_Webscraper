input = [line[:-1] for line in file("in")][1:]

case = 0

while len(input)>0:
  case += 1
  input.pop(0)
  candies = [int(x) for x in input.pop(0).split(" ")]
  best = 0
  for i in range(1, 2**len(candies) - 1):
    choice = bin(i)[2:].zfill(len(candies))
    seans = [int(candies[i]) for i in range(len(candies)) if choice[i] == "1"]
    patricks = [int(candies[i]) for i in range(len(candies)) if choice[i] == "0"]
    seans_val = sum(seans)

    seans_xor = reduce(lambda x,y: x ^ y, seans, 0)
    patricks_xor = reduce(lambda x,y: x ^ y, patricks, 0)
    if seans_xor == patricks_xor:
      best = max(best, seans_val)

  result = "NO" if best == 0 else str(best)
  print "Case #%d:" % case, result
