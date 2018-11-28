def numOfPartners(i, B): # Count all recycled partners between i and B.
  i_str = str(i)
  z = len(i_str)
  partners = set()
  for k in range(1, z):
    partner = i_str[k:z] + i_str[0:k]
    if int(partner) in range(i+1, B+1):
      partners.add(partner)
  return len(partners)


input = open("C-small-attempt0.in")
output = open("C-small-attempt0.out", "w")
input.next() #Skip the number of cases
case=1
for line in input:
  numbers = line.split(" ")
  A = int(numbers[0])
  B = int(numbers[1])
  result = 0
  # Bruteforce:
  for i in range(A, B):
    result = result + numOfPartners(i, B)
  
  output.write("Case #" + str(case) + ": " + str(result) + "\n")
  case=case+1


  
