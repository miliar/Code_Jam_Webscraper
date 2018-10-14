def flip(pancakes, w, index):
	for i in range(index, index + w):
		#print("Flip loop")
		if(pancakes[i] == "+"):
			pancakes[i] = "-"
		else:
			pancakes[i] = "+"

def test(pancakes):
	for i in pancakes:
		#print("test " + i)
		if i == "-":
			return False
	return True

t = int(input())
for i in range(1, t + 1):
  value = input();
  pancakes, flipper = [s for s in value.split(" ")];
  
  flipper = int(flipper);
  pancakes = list(pancakes);
  flips = 0;
  for p in range(0,len(pancakes)-flipper+1):
    if(pancakes[p] == "-"):
    	flip(pancakes, flipper, p);
    	flips += 1;
    	#print("Flip: {} {}".format(flips, pancakes))
  if(test(pancakes)):
	  print("Case #{}: {}".format(i, flips));
  else:
	  print("Case #{}: IMPOSSIBLE".format(i));

