
t = int(input())
for i in range(1, t + 1):
  N,R,O,Y,G,B,V = [int(s) for s in input().split(" ")];

  letters = {
  "R":R,
  "O":O,
  "Y":Y,
  "G":G,
  "B":B,
  "V":V
  };


  #remove
  letters["R"] -= letters["G"];
  letters["Y"] -= letters["V"];
  letters["B"] -= letters["O"];
  #special case! YVYV
  if letters["R"] == 0 and letters["Y"] == 0 and letters["B"] == 0:
    if letters["G"] > 0:
      if(letters["V"] > 0 or letters["O"] > 0):
        vastaus = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, vastaus))
        continue;
      else:
        vastaus = "";
        for c in range(letters["G"]):
          vastaus += "GR"
        print("Case #{}: {}".format(i, vastaus))
        continue;

    elif letters["O"] > 0:
      if(letters["V"]  > 0):
        vastaus = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, vastaus))
        continue;
      else:
        vastaus = "";
        for c in range(letters["O"]):
          vastaus += "OB"
        print("Case #{}: {}".format(i, vastaus))
        continue;
    else:
        vastaus = "";
        for c in range(letters["V"]):
          vastaus += "YV"
        print("Case #{}: {}".format(i, vastaus))
        continue;



  #
  if ((letters["G"] > 0 and letters["R"] <= 0)  or 
    (letters["V"] > 0 and letters["Y"] <= 0)  or 
    (letters["O"] > 0 and letters["B"] <= 0)):
    vastaus = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, vastaus))
    continue;

  #SOLVE
  vastaus = [];


  #small first
  while letters["R"] > 0 or letters["Y"] > 0 or letters["B"] > 0:
    can_be = ["R","Y","B"]
    if(len(vastaus) > 0):
      last = vastaus[len(vastaus) - 1];
      if(last == "R"):
        can_be = ["Y","B"]
      if(last == "Y"):
        can_be = ["R","B"]
      if(last == "B"):
        can_be = ["R","Y"]


    can_be[:] = [tup for tup in can_be if letters[tup] > 0]
    if(len(can_be) == 0):
      vastaus = "IMPOSSIBLE"
      break;

    isoin = 0
    for c in range(0, len(can_be)):
      if letters[can_be[c]] > letters[can_be[isoin]]:
        isoin = c;
    isoin_c = can_be[isoin];
    vastaus.append(isoin_c);
    letters[isoin_c] -= 1
    #print("vastaus:{} letters:{}".format(vastaus, letters));

  #Tarkista viimeinen
  if vastaus[0] == vastaus[len(vastaus) -1]:
    if B == 0 or Y == 0 or R == 0:
      vastaus = "IMPOSSIBLE"
    else:
      #Aloita perästä ja käännä parit ympäri kunnes tulee kolmas arvo vastaan, jolloin loppu, jos tulee alkuun niin ei mahdollista ratkaista,
      #print("" + str(i) + ": käännä " + vastaus);
      eka = vastaus[len(vastaus) - 1];
      toka = vastaus[len(vastaus) - 2];
      for c in range(0,len(vastaus)):
        if vastaus[len(vastaus) - (c+1)] == toka:
          vastaus[len(vastaus) - (c+1)] = eka;
        elif vastaus[len(vastaus) - (c+1)] == eka:
          vastaus[len(vastaus) - (c+1)] = toka;
        else:
          break;
  #Tarkista vastaus:
  if vastaus != "IMPOSSIBLE":
    for index in range(len (vastaus) -1):
      if(vastaus[index] == vastaus[index+1]):
        print("Virhe Case #{}: {}".format(i, vastaus));
        break;
    for c in vastaus:
      letters[c] += 1;
    if (B - letters["O"]) != letters["B"]:
      vastaus = "IMPOSSIBLE"
    if (Y - letters["V"]) != letters["Y"]:
      vastaus = "IMPOSSIBLE"
    if (R - letters["G"]) != letters["R"]:
      vastaus = "IMPOSSIBLE"

  if isinstance(vastaus, list):
      temp_v = ""
      for c in vastaus:
        temp_v += c
        while(c == "B" and letters["O"] > 0):
          temp_v += "OB"
          letters["O"] -= 1
        while c == "R" and letters["G"] > 0:
          temp_v += "GR"
          letters["G"] -= 1
        while c == "Y" and letters["V"] > 0:
          temp_v += "VY"
          letters["V"] -= 1

      vastaus = temp_v;

  #PRINT RESULT
  print("Case #{}: {}".format(i, vastaus))









