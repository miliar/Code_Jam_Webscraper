import fileinput

input = fileinput.input()

T = int(input.readline())

def myShare(score,total,newavg,N,fighteravg,Nfighters):
  if score > newavg: return 0
  else: return 100 * (fighteravg - score) / total

for t in range(1,T+1):
  line = input.readline().split(' ')
  N = int(line[0]); line = line[1:]
  scores = list(map(int, line))
  total = sum(scores)
  newavg = 2*total/N
  fighters = [s for s in scores if s <= newavg]
  fighteravg = (sum(fighters) + total) / len(fighters)

  results = list(map(lambda score:myShare(score,total,newavg,N,fighteravg,len(fighters)),scores))

  print ("Case #{0}:".format(t), end="")
  for r in results:
    print (" {0}".format(r), end="")
  print ()
