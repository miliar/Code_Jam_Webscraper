input = open("B-small-attempt0.in")
output = open("B-small-attempt0.out", "w")
input.next() #Skip the number of cases
i=1
for line in input:
  numbers = line.split(" ")
  N = int(numbers[0]) #Number of dancers
  S = int(numbers[1]) #Number of surprises
  p = int(numbers[2]) #prefered maximum
  scores = [int(numbers[j]) for j in range(3, N+3)]
  result = 0
  for score in scores:
    if score >=3*p -2: # possible without surprise
      result = result + 1
    elif score in range(3*p - 4, 3*p -3+1) and S > 0 and score > 2: # possible with surprise
      result = result + 1
      S = S - 1
  
  output.write("Case #" + str(i) + ": " + str(result) + "\n")
  i=i+1
