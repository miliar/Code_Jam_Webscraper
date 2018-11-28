def silnia(n):
  r = 1
  for i in range(1,n+1):
    r *= i
  return r

def solve(cars):
  # 1. skrocic do AB
  middles = []
  endings = set([])
  for ii,car in enumerate(cars):
    endings.add(car[0])
    endings.add(car[-1])
    if len(car)<=2:
      cars[ii] = car[0]+car[-1]
    elif len(set(car))==1:
      cars[ii] = 2*car[0]
    else:
      a = car[0]
      b = car[-1]
      i = 0
      while car[i]==a:
        i += 1
      j = len(car)-1
      while car[j]==b:
        j -= 1
      current = None
      if i<=j and car[0]==car[-1]:
        return 0 # axa
      while i<=j:
        if car[i]!=current:
          current = car[i]
          middles.append(current)
        i += 1
      cars[ii] = car[0]+car[-1]
  if len(middles)!=len(set(middles)):
    return 0
  for mid in middles:
    if mid in endings:
      return 0
  # 2. multiple usunac (zapisac mnoznik)
  mnoznik = 1
  diction = {}
  for car in cars:
    if car[0]==car[1]:
      if car in diction:
        diction[car] += 1
      else:
        diction[car] = 1
  aas = []
  for k,v in diction.items():
    mnoznik *= silnia(v)
    cars = filter(lambda a: a != k, cars)
    aas.append(k)
  
  # 3. zebrac sztywne
  firsts = map(lambda c: c[0], cars)
  seconds = map(lambda c: c[1], cars)
  if len(firsts)!=len(set(firsts)):
    return 0
  if len(seconds)!=len(set(seconds)):
    return 0
  
  letters = firsts+seconds
  for l in letters:
    if 2*l in aas:
      aas.remove(2*l)
  trains = len(set(letters))-len(cars)
  #znalezc cykle
  map1 = {}
  for car in cars:
    map1[car[0]] = car
  for car in cars:
    ind = car[1]
    while ind in map1:
      c2 = map1[ind]
      if c2==car:
        return 0
      ind = c2[1]
  
  # 4. silnia (*mnoznik)
  return silnia(trains+len(aas))*mnoznik

T = input()
for t in range(1,T+1):
  _ = raw_input()
  a = raw_input().split()
  result = solve(a)%1000000007
  print "Case #%d: %d" % (t,result)
