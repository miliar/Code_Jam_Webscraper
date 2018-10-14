from math import ceil, floor

t = int(input())
for i in range(1, t + 1):
  #READ INPUT
  ainesosia, pusseja = [int(s) for s in input().split(" ")];
  pussit = [[0 for y in range(pusseja)] for x in range(ainesosia)]
  
  annos = [int(s) for s in input().split(" ")];

  for aine in range(0, ainesosia):
    pussit[aine] = [int(s) for s in input().split(" ")];
    pussit[aine].sort()
  #SOLVE
  tulos = 0;
  for eka in pussit[0]:
    alaraja = ceil(((eka*(100/110)) / annos[0]))
    ylaraja = floor(((eka*(100/90)) / annos[0]))
    #print("pussi:{} alaraja:{} yläraja:{}".format(eka, alaraja,ylaraja))
    possible_serves_eka = [ x for x in range(alaraja,ylaraja+1)]
    possible_serves = set(possible_serves_eka);
    #print("Ekan pussi:{} M:{}".format(eka, possible_serves))

    #toinen ainesosa:
    if(ainesosia > 1):
      #filter
      for aine in range(1, ainesosia):
        possible_serves_toka = set([])
        for toka in pussit[aine]:
          alaraja = ceil(((toka*(100/110)) / annos[aine]))
          ylaraja = floor(((toka*(100/90)) / annos[aine]))
          possible_serves_toka = possible_serves_toka.union(set([ x for x in range(alaraja,ylaraja+1)]))
        #possible_serves_toka = set(possible_serves_toka)
        #print("toka {}".format(possible_serves_toka));
        #filter by second
        possible_serves = possible_serves_toka.intersection(possible_serves);

      if(len(possible_serves) == 0):
        #ei mahdollinen eka
        continue;
      else:
        will_serve = min(list(possible_serves))
        #poista se toka pussi mikä on käytössä
        for aine in range(1, ainesosia):
          for toka in pussit[aine]:
            alaraja = ceil(((toka*(100/110)) / annos[aine]))
            ylaraja = floor(((toka*(100/90)) / annos[aine]))
            if(alaraja <= will_serve and ylaraja >= will_serve):
              pussit[aine].remove(toka)
              #print("pussit:{}".format(pussit))
              break;
        tulos += 1
    else:
      if(len(possible_serves) != 0):
        tulos += 1







  #PRINT RESULT
  print("Case #{}: {}".format(i, tulos));









