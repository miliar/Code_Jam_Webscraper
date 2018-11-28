FARM_PRICE = 0
EXTRA_COOKIE = 1
CONDITION_TO_WIN = 2

def game(roles):
  guess = roles[CONDITION_TO_WIN] / 2
  if roles[CONDITION_TO_WIN] <= roles[FARM_PRICE]:
    return guess

  farm = 0
  cookies_per_second = []
  price_farm = []

  while True:

    cookies_per_second.append(2 + (roles[EXTRA_COOKIE] * farm))
    new_guess = (roles[CONDITION_TO_WIN] / cookies_per_second[farm] ) + sum(price_farm)

    price_farm.append(roles[FARM_PRICE] / cookies_per_second[farm])
    farm+=1

    if new_guess > guess:
      break
    else:
      guess = new_guess


  return guess

if __name__ == '__main__':
  number_of_cases = int(raw_input())
  #2 cookies oer second
  for k in xrange(0,number_of_cases):
    roles = [float(i) for i in raw_input().split(' ')]
    print "Case #"+str(k + 1)+": " + str(game(roles))
