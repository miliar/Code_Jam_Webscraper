def main(input, cases):
  o = open("output.out", "w")
  for i in range(cases):
    A, B, K= parseInput(input)
    output = solve(A, B, K)
    o.write("Case #{num}: {ans}".format(num=str(i+1), ans=output))
    
def parseInput(input):
  return read(input)

def solve(A, B, K):
  possible = []
  for i in range(A):
    for j in range(B):
      if i & j < K:
        possible.append((i,j))
  return str(len(possible)) + "\n"


def read(input):
  return map(int, input.readline().rstrip("\n").split(" "))

if __name__ == "__main__":
  file = open("input.in", "r")
  cases = int(file.readline())
  main(file, cases)
