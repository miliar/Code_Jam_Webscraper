def main(input, cases):
  o = open("output.out", "w")
  for i in range(cases):
    words = parseInput(input)
    output = solve(words)
    o.write("Case #{num}: {ans}".format(num=str(i+1), ans=output))
def parseInput(input):
  cases = int(read(input))
  words = []
  for i in range(cases):
    words.append(read(input))
  return words

def getCompressed(words):
  compressed = {}
  for i in words: 
    string = ""
    temp = ""
    for j in range(len(i)):
      if not i[j] == temp or temp == "":
        string = string + i[j]
        temp = i[j]
    compressed[i] = string
  return compressed
 
def solve(words):
  compressed = getCompressed(words)
  if not valid(compressed):
    return "Fegla Won\n"
  deviation, string= getOptimalSize(compressed, words)
   
  count = 0
   
  print(deviation) 
  for i in words:
    index = 0
    temp = 0
    char = ""
    for j in range(len(i)):
      if char == "":
        char = i[j]
      if char == i[j]:
        temp += 1
      else:
        count += abs(deviation[index] - temp)
        temp = 1
        char = i[j]
        index += 1
    count += abs(deviation[index] - temp) 
  
  return str(count) + "\n"
  
def getOptimalSize(compressed, words):
  string = ""
  for i in compressed:
    string = compressed[i]
    break
  deviation = []
  
  for i in range(len(string)):
    deviation.append(0)

  for i in words:
    char = "" 
    count = 0
    k = 0
    for j in range(len(i)):
      if char == "":
        char = i[j]
      if i[j] == char:
        count += 1
      else:
        char = i[j]
        deviation[k] = count + deviation[k]
        k += 1
        count = 1 
    deviation[k] = deviation[k] + count  
  
  for i in range(len(deviation)):
    deviation[i] = deviation[i]/len(words) 
  return deviation, string

def valid(compressed):
  string = ""
  for i in compressed:
    if string == "":
      string = compressed[i]
    elif not string == compressed[i]:
      return False
  return True
    

def read(input):
  return input.readline().rstrip("\n")

if __name__ == "__main__":
  file = open("input.in", "r")
  cases = int(file.readline())
  main(file, cases)
